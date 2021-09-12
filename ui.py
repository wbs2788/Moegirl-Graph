# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *



class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1013, 727)
        Form.setToolTipDuration(-1)
        Form.setStyleSheet(u"background-color: rgb(198, 255, 137);")
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(100, 30, 131, 41))
        self.comboBox.setStyleSheet(u"border:1px solid #717171;\n"
"border-radius:5px;\n"
"font: 10pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.420792 rgba(85, 255, 0, 238), stop:1 rgba(255, 255, 255, 255));\n")

        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(360, 140, 591, 451))
        self.textBrowser.setStyleSheet(u"font: 15pt \"\u6977\u4f53\";\n"
"border-image: url(1.png);\n"
"background-color: rgb(85, 255, 255);\n")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(800, 90, 93, 28))
        self.pushButton.setStyleSheet(u"border:1px solid #717171;\n"
"border-radius:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.420792 rgba(255, 247, 71, 238), stop:1 rgba(255, 255, 255, 255));\n")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(390, 90, 93, 28))
        self.pushButton_2.setStyleSheet(u"border:1px solid #717171;\n"
"border-radius:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.420792 rgba(255, 247, 71, 238), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(860, 620, 93, 28))
        self.pushButton_3.setStyleSheet(u"border:1px solid #717171;\n"
"border-radius:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.420792 rgba(255, 247, 71, 238), stop:1 rgba(255, 255, 255, 255));\n")
        self.textBrowser_2 = QTextBrowser(Form)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(50, 141, 261, 471))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(380, 30, 551, 41))
        self.lineEdit.setStyleSheet(u"font: 75 11pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.420792 rgba(255, 170, 0, 238), stop:1 rgba(255, 255, 255, 255));\n")
        self.retranslateUi(Form)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(323, 150, 20, 431))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        Form.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u756a\u5267\u2192\u89d2\u8272", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u89d2\u8272\u2192\u756a\u5267", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u58f0\u4f18\u2192\u756a\u5267", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"\u7279\u70b9\u2192\u89d2\u8272", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"\u89d2\u8272\u2192\u58f0\u4f18", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Form", u"\u89d2\u8272\u2192\u7279\u70b9", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Form", u"\u89d2\u8272\u2192\u89d2\u8272", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Form", u"\u95ee\u7b54\u6a21\u5f0f", None))


#endif // QT_CONFIG(tooltip)

        self.textBrowser.setDocumentTitle("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u67e5\u8be2", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u6e05\u9664\u8f93\u5165\u6846", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u6e05\u9664\u8f93\u51fa\u6846", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ff0000;\">\u6765\u81ea\u5f02\u4e16\u754c\u7684\u52c7\u8005\uff0c\u6b22\u8fce\u6765\u5230PWZ\u7684\u540e\u5c4b\uff01</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#ff5500;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff5500;\">\u88ab\u6f06\u9ed1\u7684\u706b\u7130\u56f4"
                        "\u7ed5\u7684\u4eba\u554a\uff0c\u548c\u6211\u6f06\u9ed1\u7684\u706b\u7130\u4f7f\u7f14\u7ed3\u604b\u4eba\u7684\u5951\u7ea6\u5427\u2026\u2026</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#ff5500;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff5500;\">\u53ea\u8981\u4f60\u8db3\u591f\u52aa\u529b\uff0c\u5c31\u53ef\u4ee5\u6253\u7834\u4e16\u754c\u58c1\u2026\u2026</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#ff5500;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff5500;\">\u6c89\u7761\u4e8e\u7ea2\u83b2"
                        "\u706b\u7130\u4e0a\u7684\u9ed1\u6697\u9f99\u7687\uff0c\u8bf7\u7528\u60a8\u7684\u5486\u54ee\uff0c\u91ca\u653e\u6211\u5427\u2026\u2026</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#ff5500;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff5500;\">\u4ee5\u6c5d\u4e4b\u9c9c\u8840\u3001\u51a0\u4ee5\u543e\u4e4b\u540d\u3001\u4e3a\u543e\u4e4b\u4ec6\uff0c\u543e\u540dPWZ\u2026\u2026</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#ff5500;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff5500;\">\u6bd4\u9ec4"
                        "\u660f\u66f4\u4e3a\u660f\u6697\u8005\uff0c\u6bd4\u8840\u6db2\u66f4\u4e3a\u8d64\u7ea2\u8005\uff0c\u5728\u65f6\u95f4\u4e4b\u6d41\u4e2d\u51fa\u73b0\u5427\uff0c\u5728\u60a8\u7684\u4f1f\u5927\u7684\u540d\u4e0b\uff0c\u6211\u5728\u8fd9\u9ed1\u6697\u4e2d\u8d77\u8a93\uff0c\u628a\u963b\u6321\u5728\u6211\u4eec\u524d\u65b9\uff0c\u6240\u6709\u7684\u611a\u8822\u4e4b\u7269\uff0c\u96c6\u5408\u4f60\u6211\u4e4b\u529b\uff0c\u8d50\u4e0e\u5176\u540c\u7b49\u7684\u6bc1\u706d\u5427\u2026\u2026</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#ff5500;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ff5500;\">\u6708\u4e4b\u7231\u795e\u4f7f\u6211\u4eec\u76f8\u9047\u3001\u6211\u4ee5\u4f1f\u5927\u9a91\u58eb\u94a2\u79d1\u5c14\u4e4b\u540d\u5728\u6b64\u4e0e\u4f60\u7f14\u7ed3\u5723\u5951"
                        "\u3002\u4ece\u6b64\u6211\u7684\u5251\u548c\u76fe\u5c06\u4e3a\u5b88\u62a4\u516c\u4e3b\u5b58\u5728\uff01\u63ed\u9732\u4e11\u6076\uff01\u6495\u6bc1\u8bc8\u9a97\uff01\u98ce\u5c06\u5316\u4f5c\u5b88\u62a4\u4f7f\uff01\u6c38\u8fdc\u966a\u4f34\u60a8\u5de6\u53f3\uff01\u4ee5\u4f1f\u5927\u7684\u6708\u795e\u540d\u4e49\u8ba9\u6211\u4eec\u7f14\u7ed3\u5951\u7ea6\uff0c\u4ece\u6b64\u5c65\u884c\u8bfa\u8a00\u2026\u2026</span></p></body></html>", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u6765\u81ea\u5f02\u4e16\u754c\u7684\u52c7\u8005\uff0c\u8bf7\u732e\u4e0a\u6c5d\u4e4b\u7cbe\u8840\uff0c\u843d\u4e0b\u7b14\u58a8\uff0c\u53ec\u5524\u5427\uff01\uff01\uff01", None))
    # retranslateUi

