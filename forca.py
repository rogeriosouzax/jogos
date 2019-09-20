
def jogar():

    print('********************************')
    print('***Bem vindo ao jogo da forca***')
    print('********************************')

    palavra_secreta = "banana"
    palavra_display = []

    enforcou = False
    acertou = False

    for c in range(0, len(palavra_secreta)):
        palavra_display.append("_ ")

    print("".join(palavra_display))

    while(not enforcou and not acertou):

        chute = input("Qual a letra?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(letra.lower() == chute.lower()):
                palavra_display[index] = chute.lower()
            index += 1

        palavra = "".join(palavra_display)
        print("".join(palavra_display))

        if(palavra_secreta != palavra):
            print("jogando...")
        else:
            print("Você acertou!")
            break

print("Fim do Jogo!")

if(__name__ == '__main__'):
    jogar()