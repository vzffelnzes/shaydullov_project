from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_password_generator(object):
    def setupUi(self, password_generator):
        password_generator.setObjectName("password_generator")
        password_generator.resize(870, 594)
        self.centralwidget = QtWidgets.QWidget(password_generator)
        self.centralwidget.setObjectName("centralwidget")
        self.generate_password = QtWidgets.QPushButton(self.centralwidget)
        self.generate_password.setGeometry(QtCore.QRect(310, 160, 221, 61))
        self.generate_password.setObjectName("generate_password")
        self.password_display = QtWidgets.QTextEdit(self.centralwidget)
        self.password_display.setGeometry(QtCore.QRect(270, 30, 301, 91))
        self.password_display.setObjectName("password_display")
        self.enter_of_password = QtWidgets.QLineEdit(self.centralwidget)
        self.enter_of_password.setGeometry(QtCore.QRect(320, 410, 201, 41))
        self.enter_of_password.setObjectName("enter_of_password")
        self.check_password = QtWidgets.QPushButton(self.centralwidget)
        self.check_password.setGeometry(QtCore.QRect(330, 470, 171, 51))
        self.check_password.setObjectName("check_password")
        self.downoload_password = QtWidgets.QPushButton(self.centralwidget)
        self.downoload_password.setGeometry(QtCore.QRect(550, 470, 161, 51))
        self.downoload_password.setObjectName("downoload_password")
        self.checking_password_display = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.checking_password_display.setGeometry(QtCore.QRect(250, 260, 331, 121))
        self.checking_password_display.setObjectName("checking_password_display")
        password_generator.setCentralWidget(self.centralwidget)

        self.retranslateUi(password_generator)
        QtCore.QMetaObject.connectSlotsByName(password_generator)

    def retranslateUi(self, password_generator):
        _translate = QtCore.QCoreApplication.translate
        password_generator.setWindowTitle(_translate("password_generator", "Генератор и проверщик паролей"))
        self.generate_password.setText(_translate("password_generator", "Сгененировать пароль"))
        self.check_password.setText(_translate("password_generator", "Проверить пароль"))
        self.downoload_password.setText(_translate("password_generator", "Загрузить пароль(и) из файла"))
