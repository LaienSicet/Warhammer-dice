from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
import sys


def nohalo():
    global SLOI, STAT, ata, t_hit, t_vynd, zav_sv, Bro,\
        q_ht, q_A, q_A_D3, q_A_D6, q_BS_WS, q_S, q_AP, \
        q_T, q_Sv, q_InSv, \
        v_sus_hi, q_sus_hi_0, q_sus_hi_1, v_let_hi, q_let_hi, v_anti, q_anti, v_dev_wo, q_dev_wo, \
        v_reroll_1_h, v_reroll_1_v, v_tvin, v_f_r_hr, v_U_F

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
    v_reroll_1_h = 0
    v_reroll_1_v = 0
    v_tvin = 0
    v_f_r_hr = 0
    v_U_F = 0


def stroki(a):
    s = ""
    for j, i in enumerate(Bro[a]):
        if j <= 45:
            s += str(i)
            s += " "
            if len(s) >= 45 and not("\n" in s):
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
    global ata, t_hit, t_vynd, zav_sv, Bro, v_reroll_1_h, v_reroll_1_v, v_tvin, v_f_r_hr, v_U_F
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
    v_reroll_1_h = fla_perevod(ui.checkBox_reroll_1_h.isChecked())
    v_reroll_1_v = fla_perevod(ui.checkBox_reroll_1_v.isChecked())
    v_tvin = fla_perevod(ui.checkBox_tvin.isChecked())
    v_f_r_hr = fla_perevod(ui.checkBox_f_r_hr.isChecked())
    v_U_F = fla_perevod(ui.checkBox_U_F.isChecked())


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


def rerol(b, x=1):
    global Bro
    B = Bro[b]
    if x == 1 and not(1 in B):
        return True
    B1 = []
    for i in B:
        if i <= x:
            B1.append(randint(1, 6))
        else:
            B1.append(i)
    Bro[b] = B1


def tvin():
    a = 1
    if q_S < q_T*2:
        a = 2
    if q_S == q_T:
        a = 3
    if q_S < q_T:
        a = 4
    if q_S*2 <= q_T:
        a = 5
    rerol(2, x=a)


def u_f(b):
    global Bro
    B = Bro[b]
    u = False
    B1 = []
    if b == 1:
        a = q_BS_WS-1
        if v_reroll_1_h == 2:
            u = True
    elif b == 2:
        a = 1
        if q_S < q_T * 2:
            a = 2
        if q_S == q_T:
            a = 3
        if q_S < q_T:
            a = 4
        if q_S * 2 <= q_T:
            a = 5
        if v_reroll_1_v == 2:
            u = True
    for i in B:
        if u == True and i == 1:
            B1.append(randint(1, 6))
        elif a != 0 and i <= a:
            B1.append(randint(1, 6))
            a = 0
        else:
            B1.append(i)
    Bro[b] = B1


def cycle():
    global ata, t_hit, t_vynd, zav_sv, Bro
    zbor_inf()
    for i in range(q_ht):
        ata += q_A + d3(broski(0, q_A_D3)) + sum(broski(0, q_A_D6))
    broski(1, ata)
    if v_f_r_hr == 2:
        rerol(1, x=q_BS_WS-1)
    elif v_U_F == 2:
        u_f(1)
    elif v_reroll_1_h == 2:
        rerol(1)
    for i in Bro[1]:
        if i >= q_BS_WS:
            t_hit += 1
        if v_sus_hi == 2 and i >= q_sus_hi_1:
            t_hit += q_sus_hi_0
        if v_let_hi == 2 and i >= q_let_hi:
            t_vynd += 1
    broski(2, t_hit)
    if v_tvin == 2:
        tvin()
    elif v_U_F == 2:
        u_f(2)
    elif v_reroll_1_v == 2:
        rerol(2)
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
        if l == 14:
            break
    STAT += "\n" *(14-L)
    SLOI = 2
    ui.setupUi(MW)


def kno_3():
    nohalo()
    ui.setupUi(MW)


class Ui_MW(object):
    def setupUi(self, MW):
        MW.setObjectName("MW")
        MW.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MW)
        self.centralwidget.setObjectName("centralwidget")
        p = 0
        #################################################################################################  неизменно
        font_1, font_2, font_3, font_4, font_5, font_6 = QtGui.QFont(), QtGui.QFont(), QtGui.QFont(), QtGui.QFont(),\
            QtGui.QFont(), QtGui.QFont()
        spisok_font = [[font_1, 16, True, 75], [font_2, 20, True, 75], [font_3, 9, False, 50], [font_4, 18, True, 75],
                       [font_5, 13, True, 75], [font_6, 12, True, 75]]
        for i in range(len(spisok_font)):
            spisok_font[i][0].setFamily("Segoe Print")
            spisok_font[i][0].setPointSize(spisok_font[i][1])
            spisok_font[i][0].setBold(spisok_font[i][2])
            spisok_font[i][0].setWeight(spisok_font[i][3])

        if p == 0:
            self.spisok_labels = []
            self.spisok_baza_l = [[20, 0, 80, 60, font_1, "  ШТ.:"], [220, 0, 80, 60, font_1, "BS/WS:"],
                                  [320, 0, 80, 60, font_1, "    S:"], [420, 0, 80, 60, font_1, "    AP:"],
                                  [105, 0, 80, 60, font_1, "    A:"], [430, 65, 15, 20, font_2, "-"],
                                  [280, 65, 15, 20, font_2, "+"], [160, 120, 41, 30, font_2, "D3"],
                                  [760, 0, 80, 60, font_1, "    Sv:"], [150, 95, 15, 20, font_2, "+"],
                                  [160, 185, 41, 30, font_2, "D6+"], [150, 160, 15, 20, font_2, "+"],
                                  [660, 0, 80, 60, font_1, "    T:"], [835, 65, 15, 20, font_2, "+"],
                                  [945, 65, 15, 20, font_2, "+"], [870, 0, 91, 60, font_1, "   In Sv:"],
                                  [50, 250, 290, 35, font_1, "[SUSTAINED HITS           ]"],
                                  [395, 255, 15, 20, font_2, "+"],
                                  [50, 300, 290, 35, font_1, "[LETHAL HITS                ]"],
                                  [395, 305, 15, 20, font_2, "+"], [395, 355, 15, 20, font_2, "+"],
                                  [50, 350, 290, 35, font_1, "[ANTI   .....................           ]"],
                                  [395, 405, 15, 20, font_2, "+"], [50, 400, 300, 35, font_1, "[DEVASTATING WOUNDS]"],
                                  [805, 760, 180, 20, font_3, "разработчик: Тарасов Д. Л."],
                                  [50, 450, 300, 35, font_1, '[re-roll "1"       HIT ROLL]'],
                                  [50, 500, 300, 35, font_1, '[re-roll "1" WOUND ROLL]'],
                                  [50, 550, 300, 35, font_1, '[full re-roll       HIT ROLL]'],
                                  [50, 600, 300, 35, font_1, '[TWIN - LINKED            ]'],
                                  [50, 650, 300, 35, font_1, '[Unparalleled  Foresight   ]']]

            for i in self.spisok_baza_l:
                self.label_0 = QtWidgets.QLabel(self.centralwidget)
                self.label_0.setGeometry(QtCore.QRect(i[0], i[1], i[2], i[3]))
                self.label_0.setFont(i[4])
                self.spisok_labels.append(self.label_0)

        ##########################################################################################################
        ############ цыфры
        self.spinBox_ht = QtWidgets.QSpinBox(self.centralwidget, value=q_ht)
        self.spinBox_A = QtWidgets.QSpinBox(self.centralwidget, value=q_A)
        self.spinBox_BS_WS = QtWidgets.QSpinBox(self.centralwidget, value=q_BS_WS)
        self.spinBox_S = QtWidgets.QSpinBox(self.centralwidget, value=q_S)
        self.spinBox_AP = QtWidgets.QSpinBox(self.centralwidget, value=q_AP)
        self.spinBox_A_D3 = QtWidgets.QSpinBox(self.centralwidget, value=q_A_D3)
        self.spinBox_A_D6 = QtWidgets.QSpinBox(self.centralwidget, value=q_A_D6)
        self.spinBox_T = QtWidgets.QSpinBox(self.centralwidget, value=q_T)
        self.spinBox_Sv = QtWidgets.QSpinBox(self.centralwidget, value=q_Sv)
        self.spinBox_InSv = QtWidgets.QSpinBox(self.centralwidget, value=q_InSv)
        self.spinBox_sus_hi_0 = QtWidgets.QSpinBox(self.centralwidget, value=q_sus_hi_0)
        self.spinBox_sus_hi_1 = QtWidgets.QSpinBox(self.centralwidget, value=q_sus_hi_1)
        self.spinBox_let_hi = QtWidgets.QSpinBox(self.centralwidget, value=q_let_hi)
        self.spinBox_anti = QtWidgets.QSpinBox(self.centralwidget, value=q_anti)
        self.spinBox_dev_wo = QtWidgets.QSpinBox(self.centralwidget, value=q_dev_wo)

        self.spis_spinBox = [[self.spinBox_ht, 30, 60, 55, 35, 0, 99], [self.spinBox_A, 125, 60, 55, 35, 0, 99],
                             [self.spinBox_BS_WS, 235, 60, 40, 35, 2, 6], [self.spinBox_S, 340, 60, 55, 35, 1, 20],
                             [self.spinBox_AP, 450, 60, 40, 35, 0, 7], [self.spinBox_A_D3, 120, 120, 40, 35, 0, 9],
                             [self.spinBox_A_D6, 120, 185, 40, 35, 0, 9], [self.spinBox_T, 680, 60, 55, 35, 1, 20],
                             [self.spinBox_Sv, 790, 60, 40, 35, 2, 7], [self.spinBox_InSv, 900, 60, 40, 35, 2, 7],
                             [self.spinBox_sus_hi_0, 285, 250, 40, 35, 1, 9], [self.spinBox_sus_hi_1, 350, 250, 40, 35, 2, 6],
                             [self.spinBox_let_hi, 350, 300, 40, 35, 2, 6], [self.spinBox_anti, 350, 350, 40, 35, 2, 6],
                             [self.spinBox_dev_wo, 350, 400, 40, 35, 2, 6]]

        for i in self.spis_spinBox:
            i[0].setGeometry(QtCore.QRect(i[1], i[2], i[3], i[4]))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(1)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(i[0].sizePolicy().hasHeightForWidth())
            i[0].setSizePolicy(sizePolicy)
            i[0].setFont(font_1)
            i[0].setRange(i[5], i[6])
        ###########################################################################################
        ##################   флаги
        self.checkBox_sus_hi, self.checkBox_let_hi, self.checkBox_anti, self.checkBox_dev_wo, self.checkBox_reroll_1_h,\
            self.checkBox_reroll_1_v, self.checkBox_f_r_hr, self.checkBox_tvin, self.checkBox_U_F =\
            QtWidgets.QCheckBox(self.centralwidget), QtWidgets.QCheckBox(self.centralwidget),\
            QtWidgets.QCheckBox(self.centralwidget), QtWidgets.QCheckBox(self.centralwidget),\
            QtWidgets.QCheckBox(self.centralwidget), QtWidgets.QCheckBox(self.centralwidget),\
            QtWidgets.QCheckBox(self.centralwidget), QtWidgets.QCheckBox(self.centralwidget), \
            QtWidgets.QCheckBox(self.centralwidget)

        self.spisok_checkBox = [[self.checkBox_sus_hi, 20, 260, 20, 20, v_sus_hi],
                                [self.checkBox_let_hi, 20, 310, 20, 20, v_let_hi],
                                [self.checkBox_anti, 20, 360, 20, 20, v_anti],
                                [self.checkBox_dev_wo, 20, 410, 20, 20, v_dev_wo],
                                [self.checkBox_reroll_1_h, 20, 460, 20, 20, v_reroll_1_h],
                                [self.checkBox_reroll_1_v, 20, 510, 20, 20, v_reroll_1_v],
                                [self.checkBox_f_r_hr, 20, 560, 20, 20, v_f_r_hr],
                                [self.checkBox_tvin, 20, 610, 20, 20, v_tvin],
                                [self.checkBox_U_F, 20, 660, 20, 20, v_U_F]]

        for i in self.spisok_checkBox:
            i[0].setGeometry(QtCore.QRect(i[1], i[2], i[3], i[4]))
            i[0].setText("")
            i[0].setCheckState(i[5])

        #################################################################################################
        ############## кнопки
        self.pushButton_KY = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_KY.setGeometry(QtCore.QRect(20, 720, 190, 60))
        self.pushButton_KY.setFont(font_4)
        self.pushButton_KY.clicked.connect(kno_1)

        self.pushButton_STAT = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_STAT.setGeometry(QtCore.QRect(230, 720, 190, 60))
        self.pushButton_STAT.setFont(font_4)
        self.pushButton_STAT.clicked.connect(kno_2)

        self.pushButton_SBROS = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SBROS.setGeometry(QtCore.QRect(540, 35, 90, 60))
        self.pushButton_SBROS.setFont(font_6)
        self.pushButton_SBROS.clicked.connect(kno_3)
        #######################################################################################################
        ###################### вывод инфы
        if SLOI == 1:
            self.label_br, self.label_at, self.label_hi, self.label_ty, self.label_sv, self.label_ITOG = \
                QtWidgets.QLabel(self.centralwidget), QtWidgets.QLabel(self.centralwidget),\
                QtWidgets.QLabel(self.centralwidget), QtWidgets.QLabel(self.centralwidget),\
                QtWidgets.QLabel(self.centralwidget), QtWidgets.QLabel(self.centralwidget)

            self.spisok_l_2 = [[self.label_br, 450, 150, 530, 50, font_1], [self.label_at, 475, 200, 530, 100, font_5],
                               [self.label_hi, 475, 325, 530, 100, font_5], [self.label_ty, 475, 450, 530, 100, font_5],
                               [self.label_sv, 475, 575, 530, 100, font_5], [self.label_ITOG, 500, 700, 290, 60, font_1]]

            for j in self.spisok_l_2:
                j[0].setGeometry(QtCore.QRect(j[1], j[2], j[3], j[4]))
                j[0].setFont(j[5])

        if SLOI == 2:
            self.label_stat_0 = QtWidgets.QLabel(self.centralwidget)
            self.label_stat_0.setGeometry(QtCore.QRect(500, 120, 300, 25))
            self.label_stat_0.setFont(font_1)

            self.label_stat = QtWidgets.QLabel(self.centralwidget)
            self.label_stat.setGeometry(QtCore.QRect(520, 150, 500, 700))
            self.label_stat.setFont(font_5)
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
        MW.setWindowTitle(_translate("MW", "Warhammer_40_000_10r.5K.2"))
        self.pushButton_KY.setText(_translate("MW", "броски"))
        self.pushButton_STAT.setText(_translate("MW", "статистика"))
        self.pushButton_SBROS.setText(_translate("MW", "сброс\nнастроек"))

        for i, l in enumerate(self.spisok_labels):
            l.setText(_translate("MW", self.spisok_baza_l[i][5]))

        if SLOI == 1:
            self.label_br.setText(_translate("MW", "броски:"))
            if len(Bro[0]) > 0:
                self.label_at.setText(_translate("MW", f"атаки [ {len(Bro[0])} ]:\n{stroki(0)}"))
            if len(Bro[1]) > 0:
                self.label_hi.setText(_translate("MW", f"хит [ {len(Bro[1])} ]:\n{stroki(1)}"))
            if len(Bro[2]) > 0:
                self.label_ty.setText(_translate("MW", f"вунд [ {len(Bro[2])} ]:\n{stroki(2)}"))
            if len(Bro[3]) > 0:
                self.label_sv.setText(_translate("MW", f"сэйв [ {len(Bro[3])} ]:\n{stroki(3)}"))
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



