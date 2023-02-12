import time
from PyQt5 import uic, QtWidgets
import pyautogui
from PyQt5.QtWidgets import QMessageBox
import keyboard

global p1, p2, clique


def mostra_posicao1():
    global p1
    p1 = pyautogui.position()
    janela.perga_pac.setText(f"({str(p1[0])}, {str(p1[1])})")


def mostra_posicao2():
    global p2
    p2 = pyautogui.position()
    janela.perga_solto.setText(f"({str(p2[0])}, {str(p2[1])})")


def iniciar():  # Faz a inicialização do processo de cliques
    global p1, p2
    print("Iniciado...")
    qnt = janela.spin.text()
    # Valida se as posições foram escolhidas e se também foi definido a quantidade de vezes que será executado.
    if qnt == "" or janela.perga_pac.text() == "" or janela.perga_solto.text() == "":
        QMessageBox.information(janela, "Atenção", "Necessário informar o número de pergaminhos que você vai\n"
                                                   "e também salvar as posições")
    else:
        global clique
        clique = 1
        qntperga_inicio = 0
        qntperga = janela.spin.text()
        time.sleep(2)
        while qntperga_inicio < int(qntperga):
            time.sleep(13)
            pyautogui.rightClick(p1[0], p1[1])
            print(f"Sala 1 do perga {qntperga_inicio + 1} iniciada...")

            while clique < 8:
                clique += 1
                print(f"Sala {clique} iniciada...")
                if clique == 8:
                    print("Sala do boss iniciada.")
                pyautogui.rightClick(p2[0], p2[1])
                time.sleep(13)
                if clique == 8:
                    print(f"Perga de número {qntperga_inicio + 1} finalizado.\n")
            clique = 1
            qntperga_inicio += 1



app = QtWidgets.QApplication([])
janela = uic.loadUi('autoclickerperga.ui')  # Cria a janela
janela.p1.clicked.connect(mostra_posicao1)
janela.p2.clicked.connect(mostra_posicao2)
janela.iniciar.clicked.connect(iniciar)
janela.spin.setMaximum(120)

janela.p1.setShortcut("1")
janela.p2.setShortcut("2")



janela.show()
app.exec()
