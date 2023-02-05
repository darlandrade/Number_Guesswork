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
    janela.hit.setEnabled(True)  # Desabilita o spinbox
    janela.enviar.setEnabled(True)  # Desabilita o botão enviar
    janela.hit.clear()
    global erros, numero_aleatorio  # Chama as variáves que serão redefinidas posteriormente.
    erros = 3
    numero_aleatorio = define_numero_aleatorio()  # Novo número aleatório


def verifica_vitoria():
    global erros
    hit = janela.hit.value()  # Adiciona o valor da spinbox à uma variável
    if hit == numero_aleatorio:  # Se o palpite estiver correto. Ganha e finaliza a partida
        janela.acertos.setText("Parabéns, você ganhou!")
        janela.dica.setText("")
        desabilita_botoes()
    else:  # Se estiver errado, diminui a quantidade de tentativas que o jogador tem.
        erros -= 1
        janela.acertos.setText(f"Você errou. Tentativas restantes {erros}")
        if erros == 0:  # Se chegar a zero uma mensagem é mostrada perguntando se quer jogar novamente.
            janela.acertos.setText("")
            desabilita_botoes()
            janela.dica.setText("")
            if QMessageBox.question(janela, "Fim de jogo", "Que pena, você não tem mais tentativas. "
                                                           "\nDeseja tentar novamente?") == QMessageBox.Yes:
                jogar_novamente()
            else:
                janela.close()
        else:
            if hit < numero_aleatorio:  # Dica simples, dizendo se o palpite foi menor ou maior do que o escolhido
                # pelo programa.
                janela.dica.setText("Você deve escolher um número maior!")
            else:
                janela.dica.setText("Você deve escolher um número menor!")


# Iniciar o aplicativo
app = QtWidgets.QApplication([])
janela = uic.loadUi('guess_window.ui')  # Inicia a janela
janela.hit.setRange(1, 50)  # Define um intervalo de número a serem escolhidos na spinbox.
janela.hit.clear()  # Deixa a spinbox vazia

janela.enviar.clicked.connect(verifica_vitoria)  # Ao clicar no botão enviar, chama a função que verificará se acertou
# ou não.

janela.show()  # Mostra a janela
app.exec()  # Executa o app
