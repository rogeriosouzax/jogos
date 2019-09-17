import adivinhacao
import forca

def executar():

    print('********************************')
    print('**Bem vindo a central de jogos**')
    print('********************************\n')

    print('Selecione o jogo que deseja jogar!\n(1) Adivinhacao (2) Forca')
    jogo_cod = int(input('Selecione: '))

    if(jogo_cod == 1):
        adivinhacao.jogar()
    elif(jogo_cod == 2):
        forca.jogar()
    else:
        print('Entrada de jogo inválida!')

if(__name__ == '__main__'):
    executar()