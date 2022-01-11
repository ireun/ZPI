# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
                               QSizePolicy, QSpinBox, QTextBrowser, QVBoxLayout,
                               QWidget, QWizard, QWizardPage, QTextEdit)
import Resources_rc

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        if not Wizard.objectName():
            Wizard.setObjectName(u"Wizard")
        Wizard.setWindowModality(Qt.NonModal)
        Wizard.resize(443, 660)
        Wizard.setMinimumSize(QSize(366, 660))
        Wizard.setMaximumSize(QSize(500, 660))
        icon = QIcon()
        icon.addFile(u":/nowyPrzedrostek/946-9465376_download-svg-download-png-sulfur-dioxide-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Wizard.setWindowIcon(icon)
        Wizard.setLocale(QLocale(QLocale.Polish, QLocale.Poland))
        Wizard.setWizardStyle(QWizard.ModernStyle)
        Wizard.setOptions(QWizard.HaveFinishButtonOnEarlyPages|QWizard.HelpButtonOnRight|QWizard.NoCancelButton)
        Wizard.setTitleFormat(Qt.AutoText)
        self.wizardPage1 = QWizardPage()
        self.wizardPage1.setObjectName(u"wizardPage1")
        self.wizardPage1.setEnabled(True)
        self.wizardPage1.setAcceptDrops(False)
        self.wizardPage1.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(self.wizardPage1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(self.wizardPage1)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setAutoFormatting(QTextEdit.AutoAll)
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setAcceptRichText(True)

        self.verticalLayout.addWidget(self.textBrowser)

        Wizard.addPage(self.wizardPage1)
        self.wizardPage2 = QWizardPage()
        self.wizardPage2.setObjectName(u"wizardPage2")
        self.gridLayout = QGridLayout(self.wizardPage2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(self.wizardPage2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(True)
        self.label_7.setWordWrap(True)

        self.gridLayout.addWidget(self.label_7, 10, 0, 1, 1)

        self.label_10 = QLabel(self.wizardPage2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)

        self.label = QLabel(self.wizardPage2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton_run = QPushButton(self.wizardPage2)
        self.pushButton_run.setObjectName(u"pushButton_run")

        self.gridLayout.addWidget(self.pushButton_run, 14, 2, 1, 1)

        self.temp_spalin_1 = QSpinBox(self.wizardPage2)
        self.temp_spalin_1.setObjectName(u"temp_spalin_1")
        self.temp_spalin_1.setMinimum(-100000)
        self.temp_spalin_1.setMaximum(100000)
        self.temp_spalin_1.setValue(10)

        self.gridLayout.addWidget(self.temp_spalin_1, 0, 1, 1, 2)

        self.label_12 = QLabel(self.wizardPage2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 9, 0, 1, 1)

        self.zasiarczenie_wegla = QSpinBox(self.wizardPage2)
        self.zasiarczenie_wegla.setObjectName(u"zasiarczenie_wegla")
        self.zasiarczenie_wegla.setMaximum(100)
        self.zasiarczenie_wegla.setValue(20)

        self.gridLayout.addWidget(self.zasiarczenie_wegla, 12, 1, 1, 2)

        self.pressure_in = QSpinBox(self.wizardPage2)
        self.pressure_in.setObjectName(u"pressure_in")

        self.gridLayout.addWidget(self.pressure_in, 8, 1, 1, 2)

        self.label_13 = QLabel(self.wizardPage2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setWordWrap(True)

        self.gridLayout.addWidget(self.label_13, 7, 0, 1, 1)

        self.temp_hydratora = QSpinBox(self.wizardPage2)
        self.temp_hydratora.setObjectName(u"temp_hydratora")
        self.temp_hydratora.setValue(50)

        self.gridLayout.addWidget(self.temp_hydratora, 5, 1, 1, 2)

        self.label_6 = QLabel(self.wizardPage2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)

        self.gridLayout.addWidget(self.label_6, 12, 0, 1, 1)

        self.label_3 = QLabel(self.wizardPage2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.poziom_p_konc = QSpinBox(self.wizardPage2)
        self.poziom_p_konc.setObjectName(u"poziom_p_konc")
        self.poziom_p_konc.setMinimum(1)
        self.poziom_p_konc.setValue(10)

        self.gridLayout.addWidget(self.poziom_p_konc, 3, 1, 1, 2)

        self.air = QSpinBox(self.wizardPage2)
        self.air.setObjectName(u"air")
        self.air.setMaximum(100)
        self.air.setValue(20)

        self.gridLayout.addWidget(self.air, 10, 1, 1, 2)

        self.label_4 = QLabel(self.wizardPage2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.temp_spalin_in = QSpinBox(self.wizardPage2)
        self.temp_spalin_in.setObjectName(u"temp_spalin_in")
        self.temp_spalin_in.setSingleStep(1)
        self.temp_spalin_in.setValue(3)

        self.gridLayout.addWidget(self.temp_spalin_in, 9, 1, 1, 2)

        self.label_2 = QLabel(self.wizardPage2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.temp_spalin_2 = QSpinBox(self.wizardPage2)
        self.temp_spalin_2.setObjectName(u"temp_spalin_2")
        self.temp_spalin_2.setValue(9)

        self.gridLayout.addWidget(self.temp_spalin_2, 2, 1, 1, 2)

        self.delta_p = QSpinBox(self.wizardPage2)
        self.delta_p.setObjectName(u"delta_p")
        self.delta_p.setValue(1)

        self.gridLayout.addWidget(self.delta_p, 7, 1, 1, 2)

        self.label_5 = QLabel(self.wizardPage2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setScaledContents(False)
        self.label_5.setWordWrap(False)

        self.gridLayout.addWidget(self.label_5, 11, 0, 1, 1)

        self.temp_spalin_in_2 = QSpinBox(self.wizardPage2)
        self.temp_spalin_in_2.setObjectName(u"temp_spalin_in_2")
        self.temp_spalin_in_2.setMaximum(100)
        self.temp_spalin_in_2.setValue(20)

        self.gridLayout.addWidget(self.temp_spalin_in_2, 11, 1, 1, 2)

        self.output = QLabel(self.wizardPage2)
        self.output.setObjectName(u"output")

        self.gridLayout.addWidget(self.output, 15, 0, 1, 3)

        Wizard.addPage(self.wizardPage2)

        self.retranslateUi(Wizard)

        QMetaObject.connectSlotsByName(Wizard)
    # setupUi

    def retranslateUi(self, Wizard):
        Wizard.setWindowTitle(QCoreApplication.translate("Wizard", u"Projekt ZPI - Instalacja Odsiarczania Spalin", None))
        self.wizardPage1.setTitle(QCoreApplication.translate("Wizard", u"Projekt ZPI - IOS", None))
        self.wizardPage1.setSubTitle("")
        self.textBrowser.setHtml(QCoreApplication.translate("Wizard", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Autorzy: </span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:10pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Amadeusz Bubniak</li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Miko\u0142aj Cypli\u0144ski</li>\n"
"<li style=\" fo"
                        "nt-size:10pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Micha\u0142 G\u0105tkowski</li>\n"
"<li style=\" font-size:10pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Tomasz Hotlo\u015b</li></ul></body></html>", None))
        self.wizardPage2.setTitle(QCoreApplication.translate("Wizard", u"Wpisz parametry algorytmu", None))
        self.wizardPage2.setSubTitle(QCoreApplication.translate("Wizard", u"W wi\u0119kszo\u015bci parametry te s\u0105 liczbami ca\u0142kowitymi.", None))
        self.label_7.setText(QCoreApplication.translate("Wizard", u"<html><head/><body><p>powietrze fluidyzacyjne</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Wizard", u"ci\u015bnienie na wlocie", None))
        self.label.setText(QCoreApplication.translate("Wizard", u"temperatura spalin", None))
        self.pushButton_run.setText(QCoreApplication.translate("Wizard", u"Uruchom", None))
        self.temp_spalin_1.setSuffix(QCoreApplication.translate("Wizard", u" \u00b0C", None))
        self.label_12.setText(QCoreApplication.translate("Wizard", u"temp. spalin przed reaktorem", None))
        self.zasiarczenie_wegla.setSuffix("")
        self.label_13.setText(QCoreApplication.translate("Wizard", u"delta p w kolanie reaktora", None))
        self.label_6.setText(QCoreApplication.translate("Wizard", u"<html><head/><body><p>zasiarczenie w\u0119gla</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Wizard", u"poziom produktu ko\u0144cowego", None))
        self.air.setSuffix(QCoreApplication.translate("Wizard", u" Nm3/h", None))
        self.label_4.setText(QCoreApplication.translate("Wizard", u"temperatura hydratora", None))
        self.temp_spalin_in.setSuffix(QCoreApplication.translate("Wizard", u" \u00b0C", None))
        self.label_2.setText(QCoreApplication.translate("Wizard", u"temperatura spalin", None))
        self.temp_spalin_2.setSuffix(QCoreApplication.translate("Wizard", u" \u00b0C", None))
        self.label_5.setText(QCoreApplication.translate("Wizard", u"temperatura spalin przed reaktorem", None))
        self.temp_spalin_in_2.setSuffix(QCoreApplication.translate("Wizard", u" \u00b0C", None))
        self.temp_spalin_in_2.setPrefix("")
        self.output.setText("")
    # retranslateUi

