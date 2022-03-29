from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import wordle_solver_qrc

class Ui_ui_wordle_solver_main_window(object):
    def setupUi(self, ui_wordle_solver_main_window):
        if not ui_wordle_solver_main_window.objectName():
            ui_wordle_solver_main_window.setObjectName(u"ui_wordle_solver_main_window")
        ui_wordle_solver_main_window.resize(1000, 600)
        font = QFont()
        font.setFamily(u"Helvetica Neue LT Std")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        ui_wordle_solver_main_window.setFont(font)
        ui_wordle_solver_main_window.setStyleSheet(u"image: url(:/assets/assets/ui-main-window.png);")
        self.ui_main_window = QWidget(ui_wordle_solver_main_window)
        self.ui_main_window.setObjectName(u"ui_main_window")
        self.ui_main_window.setStyleSheet(u"")
        self.ui_enter_button = QPushButton(self.ui_main_window)
        self.ui_enter_button.setObjectName(u"ui_enter_button")
        self.ui_enter_button.setGeometry(QRect(400, 410, 200, 70))
        self.ui_enter_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.ui_enter_button.setStyleSheet(u"QPushButton{\n"
            "	background-color: #818485;\n"
            "	image: None;\n"
            "	image: url(:/assets/assets/ui-enter-button.png);\n"
            "}\n"
            "QPushButton:hover{\n"
            "	background-color: #666766;\n"
            "}")
        self.ui_enter_button.setIconSize(QSize(200, 70))
        self.ui_enter_button.setFlat(False)
        self.ui_close_button = QPushButton(self.ui_main_window)
        self.ui_close_button.setObjectName(u"ui_close_button")
        self.ui_close_button.setGeometry(QRect(960, 0, 40, 40))
        font1 = QFont()
        font1.setKerning(False)
        self.ui_close_button.setFont(font1)
        self.ui_close_button.setAutoFillBackground(False)
        self.ui_close_button.setStyleSheet(u"QPushButton{\n"
            "	background-color: #121213;\n"
            "	image: url(:/assets/assets/ui-close-button.png);\n"
            "}\n"
            "QPushButton:hover{\n"
            "	background-color: #818485;\n"
            "}")
        self.ui_close_button.setAutoDefault(False)
        self.ui_close_button.setFlat(True)
        self.ui_minimize_button = QPushButton(self.ui_main_window)
        self.ui_minimize_button.setObjectName(u"ui_minimize_button")
        self.ui_minimize_button.setGeometry(QRect(920, 0, 40, 40))
        self.ui_minimize_button.setStyleSheet(u"QPushButton{\n"
            "	background-color: #121213;\n"
            "	image: url(:/assets/assets/ui-minimize-button.png);\n"
            "}\n"
            "QPushButton:hover{\n"
            "	background-color: #818485;\n"
            "}")
        self.ui_minimize_button.setAutoDefault(False)
        self.ui_minimize_button.setFlat(True)
        ui_wordle_solver_main_window.setCentralWidget(self.ui_main_window)

        self.retranslateUi(ui_wordle_solver_main_window)

        self.ui_minimize_button.setDefault(False)


        QMetaObject.connectSlotsByName(ui_wordle_solver_main_window)

    def retranslateUi(self, ui_wordle_solver_main_window):
        ui_wordle_solver_main_window.setWindowTitle(QCoreApplication.translate("ui_wordle_solver_main_window", u"Wordle Solver", None))
        self.ui_enter_button.setText("")
        self.ui_close_button.setText("")
        self.ui_minimize_button.setText("")

