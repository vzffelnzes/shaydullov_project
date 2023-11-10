import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QInputDialog, QFileDialog
import random
import sqlite3
from project_design import Ui_password_generator


class MyCustomError(Exception):
    pass


class MyCustomError2(Exception):
    pass


def check_password_length(password_length):
    if password_length >= 8:
        return True
    else:
        raise MyCustomError("Too short password length")


def file_is_empty(file_list):
    if len(file_list) > 0:
        return True
    else:
        raise MyCustomError2("File is empty")


def povtors_in_password(password):
    c = 0
    for i in password:
        if str(password).count(i) > 2:
            c += 1
    if c != 0:
        return True
    else:
        return False


def check_in_bd(password):
    con = sqlite3.connect("bd_with_passwords")
    cur = con.cursor()
    res = cur.execute("""SELECT dander_passwords FROM passwords WHERE dander_passwords = ?""", (password,)).fetchall()
    if len(res) == 0:
        con.close()
        return False
    else:
        con.close()
        return True


def user_password_complexity(password):
    if len(password) < 8:
        return "Пароль слишком короткий"
    lower = False
    upper = False
    cifrs = False
    special = False
    for i in password:
        if i.islower():
            lower = True
        elif i.isupper():
            upper = True
        elif i.isdigit():
            cifrs = True
        else:
            special = True
    if not lower:
        return "Пароль должен содержать буквы нижнего регистра"
    if not upper:
        return "Пароль должен содержать буквы верхнего регистра"
    if not cifrs:
        return "Пароль должен содержать хотя бы одну цифру"
    if povtors_in_password(password):
        return "Символы в пароле не должны повторяться больше 2-ух раз"
    if not special:
        return "Пароль должен содержать хотя бы один специальный символ"
    if check_in_bd(password):
        return "Пароль в базе данных утекших паролей"
    return "Пароль сложный"


class PasswordGenerator(QMainWindow, Ui_password_generator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.possible_symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                 'R',
                                 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                                 'j',
                                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0',
                                 '1',
                                 '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '*',
                                 '+', '-', '.', ':', ';', '<', '=', '>', '?', '@', '^', '_']
        self.password_display.setReadOnly(True)
        self.checking_password_display.setReadOnly(True)
        self.generate_password.clicked.connect(self.password_output_and_mistake_checking)
        self.check_password.clicked.connect(self.check_user_password)
        self.downoload_password.clicked.connect(self.downolading_passwords)

    def password_generate(self, length):
        password = ""
        for item in range(1, int(length) + 1):
            symbol = random.choice(self.possible_symbols)
            if symbol not in password:
                password += symbol
            else:
                while symbol in password:
                    symbol = random.choice(self.possible_symbols)
                password += symbol
        return password

    def password_output_and_mistake_checking(self):
        self.password_display.setText("")
        length, dialog_text = QInputDialog.getInt(self, "Желаемая длина",
                                                  "Введите длину пароля(не меньше 8), если хотите оставить "
                                                  "стандартную длину '11', не вводите ничего."
                                                  " Рекомендованная длина пароля от 11 до 17", 11)
        try:
            check_password_length(int(length))
            if dialog_text:
                self.password_display.setText(self.password_generate(int(length)))
        except MyCustomError:
            self.password_display.setText("Слишком маленькая длина пароля!"
                                          "Попробуйте еще раз!")

    def check_user_password(self):
        user_password = self.enter_of_password.text()
        self.checking_password_display.setPlainText(user_password_complexity(user_password))

    def downolading_passwords(self):
        self.checking_password_display.setPlainText("")
        fname, _ = QFileDialog.getOpenFileName(self, 'Выбрать файл с паролем', '', 'Текстовый (*.txt)')
        passwords = []
        if fname:
            with open(fname, "r") as file:
                lines = file.readlines()
        try:
            file_is_empty(lines)
            for i in lines:
                passwords.append(i.strip())
            for i in passwords:
                self.checking_password_display.appendPlainText(user_password_complexity(i))
        except MyCustomError2:
            self.checking_password_display.setPlainText("Ошибка! Файл пустой!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PasswordGenerator()
    ex.show()
    sys.exit(app.exec_())
