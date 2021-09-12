# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QTextBrowser, QComboBox,QInputDialog, QLineEdit
from ui import Ui_Form
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from py2neo import Graph,Node,Relationship,NodeMatcher
import pickle
from jieba import *
import jieba.posseg as psg



graph = Graph("bolt://localhost:7687", auth=("neo4j","yjgkg564729"))
no_answer = "没有查到QAQ，换一个再试试吧！"
def get_list(k):
    with open(k+".data","rb") as filehandle:
        return pickle.load(filehandle)
per_list = get_list("Personality")
vol_list = get_list("Vocal")
cha_list = get_list("Character")
ani_list = get_list("Anime")

load_userdict("dic.txt")




class MainWindow(QMainWindow):
    name = ''
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_Form()

        self.ui.setupUi(self)

        self.ui.lineEdit.returnPressed.connect(self.handleCalc)
        self.ui.pushButton.clicked.connect(self.handleCalc)
        self.ui.pushButton_2.clicked.connect(self.ClearInput)
        self.ui.pushButton_3.clicked.connect(self.ClearOutput)



    def getText(self,lang):
        text, okPressed = QInputDialog.getText(self, "就决定是你了！", "请输入:\n"+lang, QLineEdit.Normal, "")
        if okPressed and text != '':
            return text

    def handleCalc(self):
        info = self.ui.lineEdit.text()
        method = self.ui.comboBox.currentText()
        self.ClearInput()
        if method == '番剧→角色':
            self.com(0,info)

        elif method == '角色→番剧':
            self.com(1,info)

        elif method == '声优→番剧':
            self.com(2,info)

        elif method == '特点→角色':
            self.com(3,info)

        elif method == '角色→声优':
            self.com(4,info)

        elif method == '角色→特点':
            self.com(5,info)

        elif method == '角色→角色':
            self.com(6,info)

        elif method == '问答模式':
            self.com(7,info)
            

    def out(self,x):
        self.ui.textBrowser.append(x)
        self.ui.textBrowser.ensureCursorVisible()
    def ClearInput(self):
        self.ui.lineEdit.clear()

    def ClearOutput(self):
        self.ui.textBrowser.clear()

    def get_ans(self,ans):
            while ans != []:
                x = ans.pop()
                x = x['b']
                x = x['name']
                self.out(x)

    def ani_to_cha(self):
        ans = graph.run("MATCH (a:Anime{name:\""+self.name+"\"}) - [include] -> (b:Character) RETURN b").data()
        if ans == []:
            self.out(no_answer)
        else:
            self.out(self.name+"包含的角色有：")
        self.get_ans(ans)

    def cha_to_ani(self):
        ans = graph.run("MATCH (b:Anime) - [include] -> (a:Character{name:\""+self.name+"\"}) RETURN b").data()
        if ans == []:
            self.out(no_answer)
        else:
            self.out(self.name+"所在的番剧为：")
        self.get_ans(ans)

 
    def cha_to_vol(self):
        ans = graph.run("MATCH (b:Vocal) - [dub] -> (a:Character{name:\""+self.name+"\"}) RETURN b").data()
        if ans == []:
            self.out(no_answer)
        else:
            self.out(self.name+"的声优是：")
        self.get_ans(ans)

    def cha_to_per(self):
        ans = graph.run("MATCH (a:Character{name:\""+self.name+"\"}) - [is] -> (b:Personality) RETURN b").data()
        self.out(self.name+"的特点为：")
        self.get_ans(ans)

    def vol_to_ani(self):
        f = False
        for item in vol_list:
            if self.name in item:
                ans = graph.run("MATCH (b:Anime) - [include] -> (a:Vocal{name:'"+item+"'}) RETURN b").data()
                while ans != []:
                    if not f:
                        self.out(self.name+"的代表作品有：")
                        f = True
                    x = ans.pop()
                    x = x['b']
                    x = x['name']
                    self.out(x)
        if not f:
            self.out(no_answer)

    def per_to_cha(self):
        f = False
        for item in per_list:
            if self.ame in item:
                ans = graph.run("MATCH (b:Character) - [is] -> (a:Personality{name:'"+item+"'}) RETURN b").data()
                while ans != []:
                    if not f:
                        self.out("具有"+self.name+"特点的角色有：")
                        f = True
                    x = ans.pop()
                    x = x['b']
                    x = x['name']
                    self.out(x)
        if not f:
            self.out(no_answer)

    def cha_to_cha(self):
        f = False
        dic = {}
        ans = graph.run("MATCH (a:Character{name:\""+self.name+"\"}) - [is] -> (b:Personality) RETURN b").data() 
        cha = []
        ans_v = graph.run("MATCH (b:Vocal) - [dub] -> (a:Character{name:\""+self.name+"\"}) RETURN b").data()
        chaVoc = []
        while ans_v != []:
            cur_v = ans_v.pop()
            cur_v = cur_v['b']
            cur_v = cur_v['name']
            chaVoc.insert(0,cur_v)
        while ans != []:
            x = ans.pop()
            x = x['b']
            x = x['name']
            for item in per_list:
                if x == item:
                    new_ans = graph.run("MATCH (b:Character) - [is] -> (a:Personality{name:'"+x+"'}) RETURN b").data()
                    while new_ans != []:
                        y = new_ans.pop()
                        y = y['b']
                        y = y['name']
                        f = True
                        if y not in cha:
                            dic[y] = 0
                            cha.insert(0,y)
                        dic[y] += 1
        if not f:
            self.out(no_answer)
        else:
            dic_ordered = sorted(dic.items(),key = lambda x:x[1],reverse = False)
            cnt = 0
            self.out("与"+self.name+"相似的角色有：")
            while dic_ordered != [] and cnt < 3:
                x = dic_ordered.pop()
                if x[0] != self.name:
                    self.out(x[0]+" "+str(x[1]))
                    cnt += 1
    
    def look_up(self,l):
        items = []
        for item in l:
            if self.name in item:
                items.append(item)
        if len(items)==0:
            self.name = ''
            self.out(no_answer)
        elif len(items)==1:
            self.name = items[0]
        else:
            lang="您可能想找的是：\n"
            i = 0
            for item in items:
                lang = lang + str(i) +":"+ item + "\n"
                i = i + 1
            try:
                x = int(self.getText(lang))
                self.name = items[x]
            except ValueError:
                self.out("输入的不是数字！")
            except IndexError:
                self.out("输入的编号超出范围！")

                
    def getKey(self,lan):
        r = psg.lcut(lan)
        word = ''
        flag1 = ''
        flag2 = ''
        for item in r:
            if item.flag == 'personality' or item.flag == 'ns':
                word = item.word
                flag1 = 'personality'
                break
            elif item.flag == 'vocal':
                word = item.word
                flag1 = 'vocal'
                break
            elif item.flag == 'anime':
                word = item.word
                flag1 = 'anime'
                break
            elif item.flag == 'character' or item.flag == 'nr' or item.flag == 'nrt':
                word = item.word
                flag1 = 'character'
                break

        for item in r:
            if item.flag == 'tedian':
                flag2 = 'personality'
                break
            elif item.flag == 'shengyou':
                flag2 = 'vocal'
                break
            elif item.flag == 'fanju':
                flag2 = 'anime'
                break
            elif item.flag == 'juese':
                flag2 = 'character'
                break
        return [word,flag1,flag2] 
            

    def com(self,op,ip):
        if op == 7:
            [word,flag1,flag2] = self.getKey(ip)
            if word=='' or flag1 =='' or flag2 == '':
                self.out("主人，我不明白你在说什么ㄒoㄒ")
                return
            self.name = word
            if flag1 == 'anime' and flag2 == 'character':
                op=0
            elif flag1 == 'character' and flag2 == 'anime':
                op=1
            elif flag1 == 'vocal' and flag2 == 'anime':
                op=2
            elif flag1 == 'personality' and flag2 == 'character':
                op=3
            elif flag1 == 'character' and flag2 == 'vocal':
                op=4
            elif flag1 == 'character' and flag2 == 'personality':
                op=5
            elif flag1 == 'character' and flag2 == 'character':
                op=6
            else:
                self.out("主人，我不明白你在说什么ㄒoㄒ")
                return
        else:
            self.name = ip
        if ip == '':
            return
        if op==0:
            self.look_up(ani_list)
            if self.name != '':
                self.ani_to_cha()
        elif op==1:
            self.look_up(cha_list)
            if self.name != '':
                self.cha_to_ani()
        elif op==2:
            self.vol_to_ani()
        elif op==3:
            self.per_to_cha()
        elif op==4:
            self.look_up(cha_list)
            if self.name != '':
                self.cha_to_vol()
        elif op==5:
            self.look_up(cha_list)
            if self.name != '':
                self.cha_to_per()
        elif op==6:
            self.look_up(cha_list)
            if self.name != '':
                self.cha_to_cha()
        self.out('')

if __name__ == "__main__":

    app = QApplication([])
    mainw = MainWindow()
    mainw.show()
    app.exec_()
