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



class Search:
    name = ''

    def get_ans(self,ans):
        while ans != []:
            x = ans.pop()
            x = x['b']
            x = x['name']
            print(x)
            
    def ani_to_cha(self):
        ans = graph.run("MATCH (a:Anime{name:\""+self.name+"\"}) - [include] -> (b:Character) RETURN b").data()
        if ans == []:
            print(no_answer)
        else:
            print(self.name+"包含的角色有：")
        self.get_ans(ans)

    def cha_to_ani(self):
        ans = graph.run("MATCH (b:Anime) - [include] -> (a:Character{name:\""+self.name+"\"}) RETURN b").data()
        if ans == []:
            print(no_answer)
        else:
            print(self.name+"所在的番剧为：")
        self.get_ans(ans)

 
    def cha_to_vol(self):
        ans = graph.run("MATCH (b:Vocal) - [dub] -> (a:Character{name:\""+self.name+"\"}) RETURN b").data()
        if ans == []:
            print(no_answer)
        else:
            print(self.name+"的声优是：")
        self.get_ans(ans)

    def cha_to_per(self):
        ans = graph.run("MATCH (a:Character{name:\""+self.name+"\"}) - [is] -> (b:Personality) RETURN b").data()
        print(self.name+"的特点为：")
        self.get_ans(ans)

    def vol_to_ani(self):
        f = False
        for item in vol_list:
            if self.name in item:
                ans = graph.run("MATCH (b:Anime) - [include] -> (a:Vocal{name:'"+item+"'}) RETURN b").data()
                while ans != []:
                    if not f:
                        print(self.name+"的代表作品有：")
                        f = True
                    x = ans.pop()
                    x = x['b']
                    x = x['name']
                    print(x)
        if not f:
            print(no_answer)

    def per_to_cha(self):
        f = False
        for item in per_list:
            if self.name in item:
                ans = graph.run("MATCH (b:Character) - [is] -> (a:Personality{name:'"+item+"'}) RETURN b").data()
                while ans != []:
                    if not f:
                        print("具有"+self.name+"特点的角色有：")
                        f = True
                    x = ans.pop()
                    x = x['b']
                    x = x['name']
                    print(x)
        if not f:
            print(no_answer)

            
    def look_up(self,l):
        items = []
        for item in l:
            if self.name in item:
                items.append(item)
        if len(items)==0:
            self.name = ''
            print(no_answer)
        elif len(items)==1:
            self.name = items[0]
        else:
            i = 0
            print("您可能想找的是：")
            for item in items:
                print(str(i)+":"+item)
                i = i + 1
            try:
                x = int(input("请输入查询对象的编号："))
                self.name = items[x]
            except ValueError:
                print("输入的不是数字！")
            except IndexError:
                print("输入的编号超出范围！")

                
def getKey(lan):
    r = psg.lcut(lan)
    word = ''
    flag1 = ''
    flag2 = ''
    print(r)
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
            

def com(op,ip):
    s = Search()
    s.name = ip
    if op == 6:
        [word,flag1,flag2] = getKey(ip)
        if word=='' or flag1 =='' or flag2 == '':
            print("主人，我不明白你在说什么ㄒoㄒ")
            continue
        s.name = word
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
        else:
            print("主人，我不明白你在说什么ㄒoㄒ")
            continue

    if op==0:
        s.look_up(ani_list)
        if s.name != '':
            s.ani_to_cha()
    elif op==1:
        s.look_up(cha_list)
        if s.name != '':
            s.cha_to_ani()
    elif op==2:
        s.vol_to_ani()
    elif op==3:
        s.per_to_cha()
    elif op==4:
        s.look_up(cha_list)
        if s.name != '':
            s.cha_to_vol()
    elif op==5:
        s.look_up(cha_list)
        if s.name != '':
            s.cha_to_per()

        
            
