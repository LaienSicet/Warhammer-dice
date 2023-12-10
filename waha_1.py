from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
import sys


def nohalo():
    global SLOI, STAT, ata, t_hit, t_vynd, zav_sv, Bro,\
        q_ht, q_A, q_A_D3, q_A_D6, q_BS_WS, q_S, q_AP, \
        q_T, q_Sv, q_InSv, \
        v_sus_hi, q_sus_hi_0, q_sus_hi_1, v_let_hi, q_let_hi, v_anti, q_anti, v_dev_wo, q_dev_wo
    SLOI = 0
    #
    ata = 0
    t_hit = 0
    t_vynd = 0
    #
    zav_sv = 0
    STAT = ""
    #
    Bro = [[], [], [], []]
    #
    q_ht = 1
    q_A = 0
    q_A_D3 = 0
    q_A_D6 = 0
    q_BS_WS = 3
    q_S = 4
    q_AP = 0
    #
    q_T = 4
    q_Sv = 3
    q_InSv = 7
    #
    v_sus_hi = 0
    q_sus_hi_0 = 1
    q_sus_hi_1 = 6
    v_let_hi = 0
    q_let_hi = 6
    v_anti = 0
    q_anti = 2
    v_dev_wo = 0
    q_dev_wo = 6

def stroki(a):
    s = ""
    for j, i in enumerate(Bro[a]):
        if j <= 43:
            s += str(i)
            s += " "
            if len(s) >= 40 and not("\n" in s):
                s += "\n"
        else:
            s += "......."
            break
    return s

def fla_perevod(a):
    if a == 0 or a == False:
        return 0
    else:
        return 2

def zbor_inf():
    global q_ht, q_A, q_A_D3, q_A_D6, q_BS_WS, q_S, q_AP,\
        q_T, q_Sv, q_InSv,\
        v_sus_hi, q_sus_hi_0, q_sus_hi_1, v_let_hi, q_let_hi, v_anti, q_anti, v_dev_wo, q_dev_wo
    global ata, t_hit, t_vynd, zav_sv, Bro
    ata = 0
    t_hit = 0
    t_vynd = 0
    zav_sv = 0
    Bro = [[], [], [], []]
    q_ht = ui.spinBox_ht.value()
    q_A = ui.spinBox_A.value()
    q_A_D3 = ui.spinBox_A_D3.value()
    q_A_D6 = ui.spinBox_A_D6.value()
    q_BS_WS = ui.spinBox_BS_WS.value()
    q_S = ui.spinBox_S.value()
    q_AP = ui.spinBox_AP.value()
    q_T = ui.spinBox_T.value()
    q_Sv = ui.spinBox_Sv.value()
    q_InSv = ui.spinBox_InSv.value()
    v_sus_hi = fla_perevod(ui.checkBox_sus_hi.isChecked())
    q_sus_hi_0 = ui.spinBox_sus_hi_0.value()
    q_sus_hi_1 = ui.spinBox_sus_hi_1.value()
    v_let_hi = fla_perevod(ui.checkBox_let_hi.isChecked())
    q_let_hi = ui.spinBox_let_hi.value()
    v_anti = fla_perevod(ui.checkBox_anti.isChecked())
    q_anti = ui.spinBox_anti.value()
    v_dev_wo = fla_perevod(ui.checkBox_dev_wo.isChecked())
    q_dev_wo = ui.spinBox_dev_wo.value()

def broski(a, skolko):
    global Bro
    ret = []
    for i in range(skolko):
        br = randint(1, 6)
        Bro[a].append(br)
        ret.append(br)
    return ret

def d3(a):
    s = 0
    for i in a:
        if i == 1 or i == 2:
            s += 1
        elif i == 3 or i == 4:
            s += 2
        elif i == 5 or i == 6:
            s += 3
    return s

def Ty_Vy(a, s, t):
    if a == 1:
        return False
    elif a == 6 or (s*2 >= t and a == 5) or (s >= t and a == 4) or (s > t and a == 3) or (s >= t*2 and a == 2):
        return True
    else:
        return False

def cycle():
    global ata, t_hit, t_vynd, zav_sv, Bro
    zbor_inf()
    for i in range(q_ht):
        ata += q_A + d3(broski(0, q_A_D3)) + sum(broski(0, q_A_D6))
    broski(1, ata)
    for i in Bro[1]:
        if i >= q_BS_WS:
            t_hit += 1
        if v_sus_hi == 2 and i >= q_sus_hi_1:
            t_hit += q_sus_hi_0
        if v_let_hi == 2 and i >= q_let_hi:
            t_vynd += 1
    broski(2, t_hit)
    for i in Bro[2]:
        if v_dev_wo == 2 and (i >= q_dev_wo or (v_anti == 2 and i >= q_anti)):
            zav_sv += 1
        elif (v_anti == 2 and i >= q_anti) or Ty_Vy(i, q_S, q_T):
            t_vynd += 1
    if q_Sv + q_AP <= 6 or 7 != q_InSv:
        broski(3, t_vynd)
        for i in Bro[3]:
            if i < q_Sv + q_AP and i < q_InSv:
                zav_sv += 1
    elif q_Sv + q_AP > 6 and 7 == q_InSv:
        zav_sv += t_vynd
    return zav_sv


def stat_obr(a, b):
    a1 = [[round(a[i]/(b/100), 2), i] for i in a]
    a1.sort(reverse=True)
    return a1

def kno_1():
    global SLOI
    cycle()
    SLOI = 1
    ui.setupUi(MW)

def kno_2():
    global SLOI, STAT, ata, t_hit, t_vynd, zav_sv, Bro
    K = 5000
    zbor_inf()
    sta = []
    for i in range(K):
        sta.append(cycle())
    sta_1 = dict()
    for i in sta:
        if not i in sta_1:
            sta_1.setdefault(i, sta.count(i))
    sta_2 = stat_obr(sta_1, K)
    STAT = ""
    otstyp = round(sta_2[0][0], -1)/10
    for l, i in enumerate(sta_2):
        STAT += " "*5*int(otstyp-i[0]/10)
        STAT += f'{i[0]}% : {i[1]}\n'
        L = l
        if l == 11:
            break
    STAT += "\n" *(11-L)
    SLOI = 2
    ui.setupUi(MW)

def kno_3():
    nohalo()
    ui.setupUi(MW)


class Ui_MW(object):
    def setupUi(self, MW):
        MW.setObjectName("MW")
        MW.resize(1000, 620)
        self.centralwidget = QtWidgets.QWidget(MW)
        self.centralwidget.setObjectName("centralwidget")
        p = 0
        #################################################################################################  неизменно
        if p == 0:
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(20, 20, 80, 60))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label.setFont(font)
            self.label.setObjectName("label")
            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(220, 20, 80, 60))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_2.setFont(font)
            self.label_2.setObjectName("label_2")
            self.label_3 = QtWidgets.QLabel(self.centralwidget)
            self.label_3.setGeometry(QtCore.QRect(320, 20, 80, 60))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_3.setFont(font)
            self.label_3.setObjectName("label_3")
            self.label_4 = QtWidgets.QLabel(self.centralwidget)
            self.label_4.setGeometry(QtCore.QRect(420, 20, 80, 60))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_4.setFont(font)
            self.label_4.setObjectName("label_4")
            self.label_5 = QtWidgets.QLabel(self.centralwidget)
            self.label_5.setGeometry(QtCore.QRect(105, 20, 80, 60))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_5.setFont(font)
            self.label_5.setObjectName("label_5")
            self.label_6 = QtWidgets.QLabel(self.centralwidget)
            self.label_6.setGeometry(QtCore.QRect(430, 105, 15, 20))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.label_6.setFont(font)
            self.label_6.setObjectName("label_6")
            self.label_7 = QtWidgets.QLabel(self.centralwidget)
            self.label_7.setGeometry(QtCore.QRect(280, 105, 15, 20))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.label_7.setFont(font)
            self.label_7.setObjectName("label_7")

            self.label_8 = QtWidgets.QLabel(self.centralwidget)
            self.label_8.setGeometry(QtCore.QRect(160, 160, 41, 30))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.label_8.setFont(font)
            self.label_8.setObjectName("label_8")
            self.label_11 = QtWidgets.QLabel(self.centralwidget)
            self.label_11.setGeometry(QtCore.QRect(160, 225, 41, 30))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.label_11.setFont(font)
            self.label_11.setObjectName("label_11")
            self.label_10 = QtWidgets.QLabel(self.centralwidget)
            self.label_10.setGeometry(QtCore.QRect(150, 135, 15, 20))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.label_10.setFont(font)
            self.label_10.setObjectName("label_10")
            self.label_12 = QtWidgets.QLabel(self.centralwidget)
            self.label_12.setGeometry(QtCore.QRect(150, 200, 15, 20))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.label_12.setFont(font)
            self.label_12.setObjectName("label_12")
            self.label_9 = QtWidgets.QLabel(self.centralwidget)
            self.label_9.setGeometry(QtCore.QRect(760, 20, 80, 60))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_9.setFont(font)
            self.label_9.setObjectName("label_9")
            self.label_13 = QtWidgets.QLabel(self.centralwidget)
            self.label_13.setGeometry(QtCore.QRect(660, 20, 80, 60))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_13.setFont(font)
            self.label_13.setObjectName("label_13")
            self.label_14 = QtWidgets.QLabel(self.centralwidget)
            self.label_14.setGeometry(QtCore.QRect(835, 105, 15, 20))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.label_14.setFont(font)
            self.label_14.setObjectName("label_14")
            self.label_15 = QtWidgets.QLabel(self.centralwidget)
            self.label_15.setGeometry(QtCore.QRect(945, 105, 15, 20))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.label_15.setFont(font)
            self.label_15.setObjectName("label_15")
            self.label_16 = QtWidgets.QLabel(self.centralwidget)
            self.label_16.setGeometry(QtCore.QRect(870, 20, 91, 60))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_16.setFont(font)
            self.label_16.setObjectName("label_16")
            self.label_17 = QtWidgets.QLabel(self.centralwidget)
            self.label_17.setGeometry(QtCore.QRect(50, 290, 290, 35))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_17.setFont(font)
            self.label_17.setObjectName("label_17")
            self.label_18 = QtWidgets.QLabel(self.centralwidget)
            self.label_18.setGeometry(QtCore.QRect(395, 295, 15, 20))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.label_18.setFont(font)
            self.label_18.setObjectName("label_18")
            self.label_19 = QtWidgets.QLabel(self.centralwidget)
            self.label_19.setGeometry(QtCore.QRect(50, 340, 290, 35))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_19.setFont(font)
            self.label_19.setObjectName("label_19")
            self.label_20 = QtWidgets.QLabel(self.centralwidget)
            self.label_20.setGeometry(QtCore.QRect(395, 345, 15, 20))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.label_20.setFont(font)
            self.label_20.setObjectName("label_20")
            self.label_21 = QtWidgets.QLabel(self.centralwidget)
            self.label_21.setGeometry(QtCore.QRect(395, 395, 15, 20))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.label_21.setFont(font)
            self.label_21.setObjectName("label_21")
            self.label_22 = QtWidgets.QLabel(self.centralwidget)
            self.label_22.setGeometry(QtCore.QRect(50, 390, 290, 35))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_22.setFont(font)
            self.label_22.setObjectName("label_22")
            self.label_23 = QtWidgets.QLabel(self.centralwidget)
            self.label_23.setGeometry(QtCore.QRect(395, 445, 15, 20))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            self.label_23.setFont(font)
            self.label_23.setObjectName("label_23")
            self.label_24 = QtWidgets.QLabel(self.centralwidget)
            self.label_24.setGeometry(QtCore.QRect(50, 440, 300, 35))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_24.setFont(font)
            self.label_24.setObjectName("label_24")
            self.label_25 = QtWidgets.QLabel(self.centralwidget)
            self.label_25.setGeometry(QtCore.QRect(805, 580, 180, 20))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(9)
            self.label_25.setFont(font)
            self.label_25.setObjectName("label_25")
        ##########################################################################################################
        ############ цыфры
        self.spinBox_ht = QtWidgets.QSpinBox(self.centralwidget, value=q_ht)
        self.spinBox_ht.setGeometry(QtCore.QRect(30, 100, 55, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_ht.sizePolicy().hasHeightForWidth())
        self.spinBox_ht.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_ht.setFont(font)
        self.spinBox_ht.setObjectName("spinBox_ht")

        self.spinBox_A = QtWidgets.QSpinBox(self.centralwidget, value=q_A)
        self.spinBox_A.setGeometry(QtCore.QRect(125, 100, 55, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_A.sizePolicy().hasHeightForWidth())
        self.spinBox_A.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_A.setFont(font)
        self.spinBox_A.setObjectName("spinBox_A")

        self.spinBox_BS_WS = QtWidgets.QSpinBox(self.centralwidget, value=q_BS_WS)
        self.spinBox_BS_WS.setGeometry(QtCore.QRect(235, 100, 40, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_BS_WS.sizePolicy().hasHeightForWidth())
        self.spinBox_BS_WS.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_BS_WS.setFont(font)
        self.spinBox_BS_WS. setRange(2, 6)
        self.spinBox_BS_WS.setObjectName("spinBox_BS_WS")

        self.spinBox_S = QtWidgets.QSpinBox(self.centralwidget, value=q_S)
        self.spinBox_S.setGeometry(QtCore.QRect(340, 100, 55, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_S.sizePolicy().hasHeightForWidth())
        self.spinBox_S.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_S.setFont(font)
        self.spinBox_S.setRange(1, 20)
        self.spinBox_S.setObjectName("spinBox_S")

        self.spinBox_AP = QtWidgets.QSpinBox(self.centralwidget, value=q_AP)
        self.spinBox_AP.setGeometry(QtCore.QRect(450, 100, 40, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_AP.sizePolicy().hasHeightForWidth())
        self.spinBox_AP.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_AP.setFont(font)
        self.spinBox_AP.setRange(0, 7)
        self.spinBox_AP.setObjectName("spinBox_AP")

        self.spinBox_A_D3 = QtWidgets.QSpinBox(self.centralwidget, value=q_A_D3)
        self.spinBox_A_D3.setGeometry(QtCore.QRect(120, 160, 40, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_A_D3.sizePolicy().hasHeightForWidth())
        self.spinBox_A_D3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_A_D3.setFont(font)
        self.spinBox_A_D3.setRange(0, 9)
        self.spinBox_A_D3.setObjectName("spinBox_A_D3")

        self.spinBox_A_D6 = QtWidgets.QSpinBox(self.centralwidget, value=q_A_D6)
        self.spinBox_A_D6.setGeometry(QtCore.QRect(120, 225, 40, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_A_D6.sizePolicy().hasHeightForWidth())
        self.spinBox_A_D6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_A_D6.setFont(font)
        self.spinBox_A_D6.setRange(0, 9)
        self.spinBox_A_D6.setObjectName("spinBox_A_D6")

        self.spinBox_T = QtWidgets.QSpinBox(self.centralwidget, value=q_T)
        self.spinBox_T.setGeometry(QtCore.QRect(680, 100, 55, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_T.sizePolicy().hasHeightForWidth())
        self.spinBox_T.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_T.setFont(font)
        self.spinBox_T.setRange(1, 20)
        self.spinBox_T.setObjectName("spinBox_T")

        self.spinBox_Sv = QtWidgets.QSpinBox(self.centralwidget, value=q_Sv)
        self.spinBox_Sv.setGeometry(QtCore.QRect(790, 100, 40, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_Sv.sizePolicy().hasHeightForWidth())
        self.spinBox_Sv.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_Sv.setFont(font)
        self.spinBox_Sv.setRange(2, 7)
        self.spinBox_Sv.setObjectName("spinBox_Sv")

        self.spinBox_InSv = QtWidgets.QSpinBox(self.centralwidget, value=q_InSv)
        self.spinBox_InSv.setGeometry(QtCore.QRect(900, 100, 40, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_InSv.sizePolicy().hasHeightForWidth())
        self.spinBox_InSv.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_InSv.setFont(font)
        self.spinBox_InSv.setRange(2, 7)
        self.spinBox_InSv.setObjectName("spinBox_InSv")

        self.spinBox_sus_hi_0 = QtWidgets.QSpinBox(self.centralwidget, value=q_sus_hi_0)
        self.spinBox_sus_hi_0.setGeometry(QtCore.QRect(285, 290, 40, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_sus_hi_0.sizePolicy().hasHeightForWidth())
        self.spinBox_sus_hi_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_sus_hi_0.setFont(font)
        self.spinBox_sus_hi_0.setRange(1, 9)
        self.spinBox_sus_hi_0.setObjectName("spinBox_sus_hi_0")

        self.spinBox_sus_hi_1 = QtWidgets.QSpinBox(self.centralwidget, value=q_sus_hi_1)
        self.spinBox_sus_hi_1.setGeometry(QtCore.QRect(350, 290, 40, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_sus_hi_1.sizePolicy().hasHeightForWidth())
        self.spinBox_sus_hi_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_sus_hi_1.setFont(font)
        self.spinBox_sus_hi_1.setRange(2, 6)
        self.spinBox_sus_hi_1.setObjectName("spinBox_sus_hi_1")

        self.spinBox_let_hi = QtWidgets.QSpinBox(self.centralwidget, value=q_let_hi)
        self.spinBox_let_hi.setGeometry(QtCore.QRect(350, 340, 40, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_let_hi.sizePolicy().hasHeightForWidth())
        self.spinBox_let_hi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_let_hi.setFont(font)
        self.spinBox_let_hi.setRange(2, 6)
        self.spinBox_let_hi.setObjectName("spinBox_let_hi")

        self.spinBox_anti = QtWidgets.QSpinBox(self.centralwidget, value=q_anti)
        self.spinBox_anti.setGeometry(QtCore.QRect(350, 390, 40, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_anti.sizePolicy().hasHeightForWidth())
        self.spinBox_anti.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_anti.setFont(font)
        self.spinBox_anti.setRange(2, 6)
        self.spinBox_anti.setObjectName("spinBox_anti")

        self.spinBox_dev_wo = QtWidgets.QSpinBox(self.centralwidget, value=q_dev_wo)
        self.spinBox_dev_wo.setGeometry(QtCore.QRect(350, 440, 40, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_dev_wo.sizePolicy().hasHeightForWidth())
        self.spinBox_dev_wo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_dev_wo.setFont(font)
        self.spinBox_dev_wo.setRange(2, 6)
        self.spinBox_dev_wo.setObjectName("spinBox_dev_wo")
        ###########################################################################################
        ##################   флаги
        self.checkBox_sus_hi = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_sus_hi.setGeometry(QtCore.QRect(20, 300, 20, 20))
        self.checkBox_sus_hi.setText("")
        self.checkBox_sus_hi.setCheckState(v_sus_hi)
        self.checkBox_sus_hi.setObjectName("checkBox_sus_hi")

        self.checkBox_let_hi = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_let_hi.setGeometry(QtCore.QRect(20, 350, 20, 20))
        self.checkBox_let_hi.setText("")
        self.checkBox_let_hi.setCheckState(v_let_hi)
        self.checkBox_let_hi.setObjectName("checkBox_let__hi")

        self.checkBox_anti = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_anti.setGeometry(QtCore.QRect(20, 400, 20, 20))
        self.checkBox_anti.setText("")
        self.checkBox_anti.setCheckState(v_anti)
        self.checkBox_anti.setObjectName("checkBox_anti")

        self.checkBox_dev_wo = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_dev_wo.setGeometry(QtCore.QRect(20, 450, 20, 20))
        self.checkBox_dev_wo.setText("")
        self.checkBox_dev_wo.setCheckState(v_dev_wo)
        self.checkBox_dev_wo.setObjectName("checkBox_dev_wo")
        #################################################################################################
        ############## кнопки
        self.pushButton_KY = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_KY.setGeometry(QtCore.QRect(20, 540, 190, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_KY.setFont(font)
        self.pushButton_KY.clicked.connect(kno_1)
        self.pushButton_KY.setObjectName("pushButton")

        self.pushButton_STAT = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_STAT.setGeometry(QtCore.QRect(230, 540, 190, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_STAT.setFont(font)
        self.pushButton_STAT.clicked.connect(kno_2)
        self.pushButton_STAT.setObjectName("pushButton_2")

        self.pushButton_SBROS = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SBROS.setGeometry(QtCore.QRect(540, 55, 90, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_SBROS.setFont(font)
        self.pushButton_SBROS.clicked.connect(kno_3)
        self.pushButton_SBROS.setObjectName("pushButton_3")

        #######################################################################################################
        ###################### вывод инфы
        if SLOI == 1:
            self.label_br= QtWidgets.QLabel(self.centralwidget)
            self.label_br.setGeometry(QtCore.QRect(450, 150, 530, 50))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_br.setFont(font)
            self.label_br.setObjectName("label_at")

            self.label_at = QtWidgets.QLabel(self.centralwidget)
            self.label_at.setGeometry(QtCore.QRect(450, 200, 530, 50))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(13)
            font.setBold(True)
            font.setWeight(75)
            self.label_at.setFont(font)
            self.label_at.setObjectName("label_at")

            self.label_hi = QtWidgets.QLabel(self.centralwidget)
            self.label_hi.setGeometry(QtCore.QRect(450, 280, 530, 60))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(13)
            font.setBold(True)
            font.setWeight(75)
            self.label_hi.setFont(font)
            self.label_hi.setObjectName("label_hi")

            self.label_ty = QtWidgets.QLabel(self.centralwidget)
            self.label_ty.setGeometry(QtCore.QRect(450, 360, 530, 60))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(13)
            font.setBold(True)
            font.setWeight(75)
            self.label_ty.setFont(font)
            self.label_ty.setObjectName("label_ty")

            self.label_sv = QtWidgets.QLabel(self.centralwidget)
            self.label_sv.setGeometry(QtCore.QRect(450, 440, 530, 60))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(13)
            font.setBold(True)
            font.setWeight(75)
            self.label_sv.setFont(font)
            self.label_sv.setObjectName("label_sv")

            self.label_ITOG = QtWidgets.QLabel(self.centralwidget)
            self.label_ITOG.setGeometry(QtCore.QRect(500, 520, 290, 60))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_ITOG.setFont(font)
            self.label_ITOG.setObjectName("label_ITOG")
        if SLOI == 2:
            self.label_stat_0 = QtWidgets.QLabel(self.centralwidget)
            self.label_stat_0.setGeometry(QtCore.QRect(500, 150, 300, 25))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label_stat_0.setFont(font)
            self.label_stat_0.setObjectName("label_at")

            self.label_stat = QtWidgets.QLabel(self.centralwidget)
            self.label_stat.setGeometry(QtCore.QRect(520, 130, 500, 500))
            font = QtGui.QFont()
            font.setFamily("Segoe Print")
            font.setPointSize(13)
            font.setBold(True)
            font.setWeight(75)
            self.label_stat.setFont(font)
            self.label_stat.setObjectName("label_at")
        #####################################################################################################

        MW.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MW)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MW.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MW)
        self.statusbar.setObjectName("statusbar")
        MW.setStatusBar(self.statusbar)

        self.retranslateUi(MW)
        QtCore.QMetaObject.connectSlotsByName(MW)

    def retranslateUi(self, MW):
        _translate = QtCore.QCoreApplication.translate
        MW.setWindowTitle(_translate("MW", "Warhammer_40_000_10r.5K.1"))
        self.label.setText(_translate("MW", "  ШТ.:"))
        self.label_2.setText(_translate("MW", "BS/WS:"))
        self.label_3.setText(_translate("MW", "    S:"))
        self.label_4.setText(_translate("MW", "    AP:"))
        self.label_5.setText(_translate("MW", "    A:"))
        self.label_6.setText(_translate("MW", "-"))
        self.label_7.setText(_translate("MW", "+"))
        self.label_8.setText(_translate("MW", "D3"))
        self.label_11.setText(_translate("MW", "D6+"))
        self.label_10.setText(_translate("MW", "+"))
        self.label_12.setText(_translate("MW", "+"))
        self.label_9.setText(_translate("MW", "    Sv:"))
        self.label_13.setText(_translate("MW", "    T:"))
        self.label_14.setText(_translate("MW", "+"))
        self.label_15.setText(_translate("MW", "+"))
        self.label_16.setText(_translate("MW", "   In Sv:"))
        self.label_17.setText(_translate("MW", "[SUSTAINED HITS           ]"))
        self.label_18.setText(_translate("MW", "+"))
        self.label_19.setText(_translate("MW", "[LETHAL HITS                ]"))
        self.label_20.setText(_translate("MW", "+"))
        self.label_21.setText(_translate("MW", "+"))
        self.label_22.setText(_translate("MW", "[ANTI   .....................           ]"))
        self.label_23.setText(_translate("MW", "+"))
        self.label_24.setText(_translate("MW", "[DEVASTATING WOUNDS]"))
        self.pushButton_KY.setText(_translate("MW", "броски"))
        self.pushButton_STAT.setText(_translate("MW", "статистика"))
        self.pushButton_SBROS.setText(_translate("MW", "сброс\nнастроек"))

        self.label_25.setText(_translate("MW", "разработчик: Тарасов Д. Л."))

        if SLOI == 1:
            self.label_br.setText(_translate("MW", "броски:"))
            if len(Bro[0]) > 0:
                self.label_at.setText(_translate("MW", f"атаки [ {len(Bro[0])} ]: {stroki(0)}"))
            if len(Bro[1]) > 0:
                self.label_hi.setText(_translate("MW", f"хит [ {len(Bro[1])} ]: {stroki(1)}"))
            if len(Bro[2]) > 0:
                self.label_ty.setText(_translate("MW", f"вунд [ {len(Bro[2])} ]: {stroki(2)}"))
            if len(Bro[3]) > 0:
                self.label_sv.setText(_translate("MW", f"сэйв [ {len(Bro[3])} ]: {stroki(3)}"))
            self.label_ITOG.setText(_translate("MW", f"ИТОГО:   {zav_sv}   провалов."))
        if SLOI == 2:
            self.label_stat_0.setText(_translate("MW", "статистика:"))
            self.label_stat.setText(_translate("MW", STAT))

if __name__ == "__main__":
    nohalo()
    app = QtWidgets.QApplication(sys.argv)
    MW = QtWidgets.QMainWindow()
    ui = Ui_MW()
    ui.setupUi(MW)
    MW.show()
    sys.exit(app.exec_())
