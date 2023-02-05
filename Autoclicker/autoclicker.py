import time
from PyQt5 import uic, QtWidgets
import pyautogui
from PyQt5.QtWidgets import QMessageBox

global p1, p2


def mostra_posicao1():
    global p1
    p1 = pyautogui.position()
    janela.posi1.setText(f"({str(p1[0])}, {str(p1[1])})")


def mostra_posicao2():
    global p2
    p2 = pyautogui.position()
    janela.posi2.setText(f"({str(p2[0])}, {str(p2[1])})")


def iniciar():  # Faz a inicialização do processo de cliques
    global p1, p2
    qnt = janela.qnt.text()
    # Valida se as posições foram escolhidas e se também foi definido a quantidade de vezes que será executado.
    if qnt == "" or janela.posi1.text() == "" or janela.posi2.text() == "":
        QMessageBox.information(janela, "Atenção", "Necessário informar o número de vezes para clicar\n"
                                                   "e também salvar as posições")
    else:
        clique = 0
        time.sleep(2)
        # pyautogui.hotkey("alt", "tab")
        while clique < int(janela.qnt.text()):
            clique += 1
            time.sleep(0.08)
            pyautogui.moveTo(p1[0], p1[1])
            pyautogui.click(p1[0], p1[1])
            time.sleep(0.08)
            pyautogui.moveTo(p2[0], p2[1])
            pyautogui.click(p2[0], p2[1])


app = QtWidgets.QApplication([])
janela = uic.loadUi('autoclicker.ui')  # Cria a janela
janela.b1.clicked.connect(mostra_posicao1)
janela.b2.clicked.connect(mostra_posicao2)
janela.iniciar.clicked.connect(iniciar)

janela.b1.setShortcut("1")
janela.b2.setShortcut("2")
janela.iniciar.setShortcut('enter')

janela.show()
app.exec()
