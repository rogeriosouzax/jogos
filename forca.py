from random import randrange

def jogar():

    print('********************************')
    print('***Bem vindo ao jogo da forca***')
    print('********************************')

    with open("frutas", mode="r") as fruta:
        frutas = fruta.read().split("\n")

    index = randrange(0, len(frutas))

    palavra_secreta = frutas[index]
    palavra_display = ["_ " for letra in palavra_secreta]
    erros = 0

    enforcou = False
    acertou = False

    print("".join(palavra_display))

    while not enforcou and not acertou:

        chute = input("Qual a letra?")
        chute = chute.strip().lower()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if letra == chute:
                    palavra_display[index] = chute
                index += 1
        else:
            erros += 1

        palavra = "".join(palavra_display)
        print("".join(palavra_display))
        print("Você errou {}/5 vezes...".format(erros))

        if palavra_secreta != palavra and erros < 5:
            print("jogando...")
        elif erros == 5:
            print("Você perdeu!")
            enforcou = True
        else:
            print("Você venceu!")
            acertou = True


print("Fim do Jogo!")

if __name__ == "__main__":
    jogar()
