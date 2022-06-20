from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox
import sys
import networkx as nx


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Кодирование/Декодирование сверточных кодов")
        MainWindow.resize(1200, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        #self.label=QLabel("Green",self)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(40, 40, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(370, 40, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(730, 30, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(1050, 20, 61, 81))
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(510, 110, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(40, 210, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(260, 40, 42, 31))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(620, 40, 42, 31))
        self.spinBox_2.setObjectName("spinBox_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 260, 281, 87))
        self.textEdit_2.setTabChangesFocus(False)
        self.textEdit_2.setReadOnly(False)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(460, 210, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setScaledContents(False)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(460, 260, 281, 87))
        self.textEdit_3.setTabChangesFocus(False)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(930, 210, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setScaledContents(False)
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(850, 260, 281, 87))
        self.textEdit_4.setTabChangesFocus(False)
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(490, 390, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setScaledContents(False)
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setEnabled(True)
        self.label_9.setGeometry(QtCore.QRect(70, 460, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setScaledContents(False)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(30, 500, 281, 87))
        self.textEdit_5.setTabChangesFocus(False)
        self.textEdit_5.setReadOnly(False)
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(460, 500, 281, 87))
        self.textEdit_6.setTabChangesFocus(False)
        self.textEdit_6.setReadOnly(True)
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setEnabled(True)
        self.label_10.setGeometry(QtCore.QRect(460, 460, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setScaledContents(False)
        self.label_10.setWordWrap(False)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(910, 460, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setScaledContents(False)
        self.label_11.setWordWrap(False)
        self.label_11.setObjectName("label_11")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(850, 500, 281, 87))
        self.textEdit_7.setTabChangesFocus(False)
        self.textEdit_7.setReadOnly(True)
        self.textEdit_7.setObjectName("textEdit_7")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(520, 70, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setUnderline(True)
        self.commandLinkButton.setFont(font)
        icon = QtGui.QIcon.fromTheme("123")
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 280, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 530, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.buttons()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Количество регистров"))
        self.label_2.setText(_translate("MainWindow", "Количество сумматоров"))
        self.label_3.setText(_translate("MainWindow", "Список регистров для сумматоров"))
        self.label_4.setText(_translate("MainWindow", "Кодирование"))
        self.label_5.setText(_translate("MainWindow", "Текст для кодирования"))
        self.label_6.setText(_translate("MainWindow", "Информационное слово"))
        self.label_7.setText(_translate("MainWindow", "Кодовое слово"))
        self.label_8.setText(_translate("MainWindow", "Декодирование"))
        self.label_9.setText(_translate("MainWindow", "Кодовое слово"))
        self.label_10.setText(_translate("MainWindow", "Информационное слово"))
        self.label_11.setText(_translate("MainWindow", "Изначальный текст"))
        self.pushButton.setText(_translate("MainWindow", "Кодировать"))
        self.pushButton_2.setText(_translate("MainWindow", "Декодировать"))

    def buttons(self):
        self.pushButton.clicked.connect(lambda: self.codir(self.spinBox.text(), self.spinBox_2.text(), self.textEdit.toPlainText(), self.textEdit_2.toPlainText()))
        self.pushButton_2.clicked.connect(lambda: self.decodir(self.spinBox.text(), self.spinBox_2.text(), self.textEdit.toPlainText(), self.textEdit_5.toPlainText(),self.textEdit_2.toPlainText()))

    def codir(self, spinBox, spinBox_2, textEdit, textEdit_2):
        str_to_conv = textEdit_2
        kolvo_registrov = int(spinBox)
        bin1_result = ''.join(format(ord(x), 'b') for x in str_to_conv)
        self.textEdit_3.setText(bin1_result)#выводит информационное слово
        bin2_result = list(bin1_result)
        for i in range(len(bin1_result)):
            bin2_result[i] = int(bin2_result[i])
        gr = []
        for i in range(kolvo_registrov):
            gr.append(0)  # список для сумматоров. Из этого списка берутся эл-ты и складываются на сумматоре
        zakodirovannaya_posledovatelnost = []  # в этот список будем класть элементы, получившиеся на сумматоре(сумматорах)

        kolvo_summatorov = int(spinBox_2)
        spisok = []
        SR=textEdit

        if str_to_conv == "":
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Отсутствует текст для кодирования!")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
        if SR == "":
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Пустое поле для перечня регистров")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()

        SR = SR.split("\n")
        for i in range(len(SR)):
            SR[i] = SR[i].split()
        for i in range(len(SR)):
            for j in range(len(SR[i])):
                SR[i][j] = int(SR[i][j]) - 1 #либо spisok.append(sr[i][j])

        # Теперь пишем алгоритм для сумматора. Если сумматоров>1, то сделать функцию.
        for i in range(len(bin2_result)):
            gr.insert(0, bin2_result[i])
            for j in range(kolvo_summatorov):
                e = 0
                for k in range(len(SR[j])):
                    e = e + gr[SR[j][k]]
                    k = k + 1
                if (e % 2 == 0):
                    e = 0
                else:
                    e = 1
                zakodirovannaya_posledovatelnost.append(e)
                j = j + 1
        kod = []
        for i in range(len(zakodirovannaya_posledovatelnost)):
            kod.append(zakodirovannaya_posledovatelnost[i])
        zakodirovannaya_posledovatelnost1 = ''.join(str(n) for n in zakodirovannaya_posledovatelnost)
        self.textEdit_4.setText((zakodirovannaya_posledovatelnost1))

    def decodir(self, spinBox, spinBox_2, textEdit, textEdit_5,textEdit_2):
        str_to_conv = textEdit_2
        kolvo_registrov = int(spinBox)
        bin_result = ' '.join(format(ord(x), 'b') for x in str_to_conv)
        bin1_result = ''.join(format(ord(x), 'b') for x in str_to_conv)
        bin2_result = list(bin1_result)
        for i in range(len(bin1_result)):
            bin2_result[i] = int(bin2_result[i])
        gr = []
        for i in range(kolvo_registrov):
            gr.append(0)  # список для сумматоров. Из этого списка берутся эл-ты и складываются на сумматоре
        zakodirovannaya_posledovatelnost = []  # в этот список будем класть элементы, получившиеся на сумматоре(сумматорах)

        kolvo_summatorov = int(spinBox_2)
        SR = textEdit
        SR = SR.split("\n")
        for i in range(len(SR)):
            SR[i] = SR[i].split()
        for i in range(len(SR)):
            for j in range(len(SR[i])):
                SR[i][j] = int(SR[i][j]) - 1  # либо spisok.append(sr[i][j])

        # Теперь пишем алгоритм для сумматора. Если сумматоров>1, то сделать функцию.
        for i in range(len(bin2_result)):
            gr.insert(0, bin2_result[i])
            for j in range(kolvo_summatorov):
                e = 0
                for k in range(len(SR[j])):
                    e = e + gr[SR[j][k]]
                    k = k + 1
                if (e % 2 == 0):
                    e = 0
                else:
                    e = 1
                zakodirovannaya_posledovatelnost.append(e)
                j = j + 1
        kod = []
        for i in range(len(zakodirovannaya_posledovatelnost)):
            kod.append(zakodirovannaya_posledovatelnost[i])
        zakodirovannaya_posledovatelnost1 = ''.join(str(n) for n in zakodirovannaya_posledovatelnost)



        zakodirovannaya_posledovatelnost2=textEdit_5
        zakodirovannaya_posledovatelnost3=list(zakodirovannaya_posledovatelnost2)
        for i in range(len(zakodirovannaya_posledovatelnost3)):
            zakodirovannaya_posledovatelnost3[i]=int(zakodirovannaya_posledovatelnost3[i])
        res = []
        for i in range(2 ** (kolvo_registrov - 1)):
            s = ''
            for j in range(kolvo_registrov - 1):
                s = str(i % 2) + s
                i = i // 2
            res.append(s)

        gruppa = []
        for i in range(len(res)):
            for j in range(kolvo_registrov - 1):
                gruppa.append(int(res[i][j]))
        #print("gruppa = ", gruppa)  # целочисленные значения битовой последовательности типа 00,01,10,11

        gr1 = []
        gruppa1 = []

        for x in range(len(res)):
            for i in range(kolvo_registrov - 1):
                gruppa1.append(gruppa[i])
            for j in range(2):
                gruppa1.insert(0, j)
                for i in range(kolvo_summatorov):
                    k = 0
                    for l in range(len(SR[i])):
                        k = k + gruppa1[SR[i][l]]
                    k = k % 2
                    gr1.append(k)
                gruppa1.pop(0)
            gruppa1 = []
            for y in range(kolvo_registrov - 1):
                gruppa.pop(0)

        #print("gr1(числа над линиями витерби)= ", gr1)

        # пишем код для расчета веса хэминга
        zakod_posl = []
        sum = 0
        gr2 = []
        for i in range(len(zakodirovannaya_posledovatelnost3) // kolvo_summatorov):
            for z in range(kolvo_summatorov):
                zakod_posl.append(zakodirovannaya_posledovatelnost3[0])
                zakodirovannaya_posledovatelnost3.pop(0)
            for j in range(len(gr1)):
                for x in range(kolvo_summatorov):
                    if (gr1[x] != zakod_posl[x]):
                        sum = sum + 1
                    else:
                        sum = sum
                    x = x + 1
                gr2.append(sum)
                for p in range(kolvo_summatorov):
                    gr1.append(gr1.pop(0))
                sum = 0
                x = 0
            for q in range(kolvo_summatorov):
                zakod_posl.pop(0)
        #print("Вес хэминга=", gr2)
        #print(len(gr2))

        #print("len(kod)= ", len(kod))
        #print("len(gr1)=", len(gr1))

        # print("gr2(вес хэминга)=",gr2)#почему-то выводит в 2 раза больше чисел, чем нужно
        gr4 = []
        if (kolvo_summatorov == 1):
            for i in range(len(gr2)):
                gr4.append(gr2[i])
        else:
            for i in range(len(kod) // kolvo_summatorov):
                for j in range(len(gr1) // kolvo_summatorov):
                    gr4.append(gr2[0])
                    gr2.pop(0)
                for k in range(len(gr1) - (len(gr1) // kolvo_summatorov)):
                    gr2.pop(0)

        #print("Вес хэминга = ", gr4)
        #print(len(gr4))

        # строим граф. Его вес рассчитали зараннее (gr4)
        # сначала создадим узлы графа, затем ребра

        G = nx.DiGraph()
        nodes = []

        for i in range(len(kod) // kolvo_summatorov + 1):
            for j in range(len(res)):
                nodes.append(res[j] + "(" + str(i) + ")")
        G.add_nodes_from(nodes)
        #print("Узлы = ", nodes)

        m = []
        i = 0
        for i in range(len(gr4) // 2):
            for j in range(2):
                m.append(int(i))
            i = i + 1
        #print(m)
        #print(len(m))

        n = []
        for s_ in range(1, len(bin1_result) + 1):
            for j in range(len(res) // 2):
                for j_ in range(2):
                    n.append(int(s_) * len(res) + j)
                    n.append(int(s_) * len(res) + len(res) // 2 + j)
                j = j + 1
            s_ = s_ + 1

        #print(n)
        #print(len(n))
        ##########################################################создаем ребра
        for i in range(len(gr4)):
            G.add_edge(nodes[m[i]], nodes[n[i]], weight=gr4[i])
            i = i + 1
        ##########################################################

        gr2_ = []
        min = 100
        for i in range(1, len(res) + 1):
            if (nx.dijkstra_path_length(G, nodes[0], nodes[-1 * i]) <= min):
                min = nx.dijkstra_path_length(G, nodes[0], nodes[-1 * i])
                aa = nx.dijkstra_path(G, nodes[0], nodes[-1 * i])
            i = i + 1
        #print(aa)
        for i in range(1, len(bin1_result) + 1):
            gr2_.append(aa[i][0])


        gr5 = []
        for i in range(len(bin_result)):
            if bin_result[i] == " ":
                gr5.append(i)
        #print("gr5", gr5)
        # преобразуем последовательность в изначальную строку
        for i in range(len(str_to_conv) - 1):
            gr2_.insert(gr5[i], " ")
        strOfStrings = ''.join(gr2_)
        self.textEdit_6.setText(strOfStrings)
        revert = ''.join([chr(int(s, 2)) for s in strOfStrings.split()])  # из двоичной в обычную
        self.textEdit_7.setText(revert)



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def openinf():
    global Form
    Form = QtWidgets.QWidget()
    ui.setupUi(Form)
    Form.show()

ui.commandLinkButton.clicked.connect(openinf)

sys.exit(app.exec_())