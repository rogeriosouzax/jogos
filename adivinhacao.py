from random import randrange

def jogar():

    print('********************************')
    print('Bem vindo ao jogo de adivinhação')
    print('********************************')

    numero_secreto = randrange(1,11)
    total_pontos = 100

    print('Selecione o nível (1) Fácil (2) Moderado (3)Difícil')
    nivel_dificuldade = int(input('Nível: '))

    if(nivel_dificuldade == 1):
        total_tentativas = 6
    elif(nivel_dificuldade == 2):
        total_tentativas = 4
    else:
        total_tentativas = 2


    for tentativas in range(1, total_tentativas + 1):
        print('Tentativa: {}/{}'.format(tentativas,total_tentativas))
        chute = int(input('Digite seu numero entre 1 a 10: '))

        if(chute < 1 or chute > 10):
            print('Seu numero está fora do intervalo de 1 - 10!')
            continue

        acerto = chute == numero_secreto
        maior = chute > numero_secreto

        if(acerto):
            print('Parabéns você acertou!')
            break
        elif(maior):
            print('Você chutou alto.')
            total_pontos = total_pontos - abs(chute - numero_secreto)
        else:
            print('Você chutou baixo')
            total_pontos = total_pontos - abs(chute - numero_secreto)

    print('Fim do jogo! \nO numero secreto era: {} \nSua pontuação foi: {}'.format(numero_secreto,total_pontos))

if(__name__ == '__main__'):
    jogar()
