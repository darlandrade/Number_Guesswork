from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPalette, QColor


def one():
    current_text = janela.entered.text()
    print(current_text)
    janela.entered.setText(current_text + "1")


def two():
    current_text = janela.entered.text()
    print(current_text)
    janela.entered.setText(current_text + "2")


def three():
    current_text = janela.entered.text()
    print(current_text)
    janela.entered.setText(current_text + "3")


def four():
    current_text = janela.entered.text()
    print(current_text)
    janela.entered.setText(current_text + "4")


def five():
    current_text = janela.entered.text()
    print(current_text)
    janela.entered.setText(current_text + "5")


def six():
    current_text = janela.entered.text()
    print(current_text)
    janela.entered.setText(current_text + "6")


def seven():
    current_text = janela.entered.text()
    print(current_text)
    janela.entered.setText(current_text + "7")


def eight():
    current_text = janela.entered.text()
    print(current_text)
    janela.entered.setText(current_text + "8")


def nine():
    current_text = janela.entered.text()
    print(current_text)
    janela.entered.setText(current_text + "9")


def zero():
    current_text = janela.entered.text()
    print(current_text)
    janela.entered.setText(current_text + "0")


def comma():
    current_text = janela.entered.text()
    print(current_text)
    janela.entered.setText(current_text + ",")


def dot():
    current_text = janela.entered.text()
    print(current_text)
    janela.entered.setText(current_text + ".")


def plus():
    if janela.result.text():
        current_text = janela.result.text() + janela.entered.text()
        janela.result.setText(current_text + "+")
        clear_entered()
    else:
        current_text = janela.entered.text()
        janela.result.setText(current_text + "+")
        clear_entered()


def subtract():
    if janela.result.text():
        current_text = janela.result.text() + janela.entered.text()
        janela.result.setText(current_text + "-")
        clear_entered()
    else:
        current_text = janela.entered.text()
        janela.result.setText(current_text + "-")
        clear_entered()


def divide():
    if janela.result.text():
        current_text = janela.result.text() + janela.entered.text()
        janela.result.setText(current_text + "/")
        clear_entered()
    else:
        current_text = janela.entered.text()
        janela.result.setText(current_text + "/")
        clear_entered()


def times():
    if janela.result.text():
        current_text = janela.result.text() + janela.entered.text()
        janela.result.setText(current_text + "*")
        clear_entered()
    else:
        current_text = janela.entered.text()
        janela.result.setText(current_text + "*")
        clear_entered()


def equals():
    if janela.result.text():
        calculo = eval(janela.result.text() + janela.entered.text())

        janela.result.setText(str(calculo))
    else:
        QMessageBox.information(janela, "Campo em branco", "Não há nada para ser calculado")

    janela.entered.clear()


def clear_entered():
    janela.entered.clear()


def clear_all():
    janela.entered.clear()
    janela.result.clear()


app = QtWidgets.QApplication([])
janela = uic.loadUi('calculator.ui')  # Cria a janela

# Números
janela.one.clicked.connect(one)
janela.one.setShortcut('1')
janela.two.clicked.connect(two)
janela.three.clicked.connect(three)
janela.four.clicked.connect(four)
janela.five.clicked.connect(five)
janela.six.clicked.connect(six)
janela.seven.clicked.connect(seven)
janela.eight.clicked.connect(eight)
janela.nine.clicked.connect(nine)
janela.zero.clicked.connect(zero)
# Comma and dot
janela.comma.setEnabled(False)
janela.dot.clicked.connect(dot)
janela.clear.clicked.connect(clear_all)
# Operators
janela.plus.clicked.connect(plus)
janela.divide.clicked.connect(divide)
janela.subtract.clicked.connect(subtract)
janela.times.clicked.connect(times)

# Equals
janela.equals.clicked.connect(equals)

########################################
janela.show()  # Mostra a janela
app.exec()  # Executa a aplicação
