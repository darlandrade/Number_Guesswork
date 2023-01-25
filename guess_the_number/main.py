import random

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox


def define_numero_aleatorio():
    return random.choice([x for x in range(1, 51)])


erros = 3
numero_aleatorio = define_numero_aleatorio()  # Escolhe um número para o jogador adivinhar.


def desabilita_botoes():
    janela.hit.setEnabled(False)
    janela.enviar.setEnabled(False)


def jogar_novamente():
    janela.hit.setEnabled(True)
    janela.enviar.setEnabled(True)
    global erros, numero_aleatorio
    erros = 3
    numero_aleatorio = define_numero_aleatorio()


def verifica_vitoria():
    global erros
    hit = janela.hit.value()  # Adiciona o valor da spinbox à uma variável
    if hit == numero_aleatorio:  # Se o palpite estiver correto. Ganha e finaliza a partida
        janela.acertos.setText("Parabéns, você ganhou!")
        janela.dica.setText("")
        desabilita_botoes()
    else:
        erros -= 1
        janela.acertos.setText(f"Você errou. Tentativas restantes {erros}")
        if erros == 0:
            janela.acertos.setText("")
            desabilita_botoes()
            janela.dica.setText("")
            if QMessageBox.question(janela, "Fim de jogo", "Que pena, você não tem mais tentativas. "
                                                           "\nDeseja tentar novamente?") == QMessageBox.Yes:
                jogar_novamente()
            else:
                janela.close()
        else:
            if hit < numero_aleatorio:
                janela.dica.setText("Você deve escolher um número maior!")
            else:
                janela.dica.setText("Você deve escolher um número menor!")


# Iniciar o aplicativo
app = QtWidgets.QApplication([])
janela = uic.loadUi('guess_window.ui')  # Inicia a janela
janela.hit.setRange(1, 50)  # Define um intervalo de número a serem escolhidos.
janela.hit.clear()  # Deixa a spinbox vazia

janela.enviar.clicked.connect(verifica_vitoria)  # Valida se acertou ou não

janela.show()
app.exec()
