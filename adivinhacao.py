import random

def jogar():
    print("***********************************************")
    print("*                                             *")
    print("*      Bem Vindo ao Jogo de Adivinhação       *")
    print("*                                             *")
    print("***********************************************")

    numero_secreto = random.randrange(1, 101)
    numero_de_tentativas = 0
    pontuacao = 1000

    print("Qual o nível de dificuldade? ")
    print("(1) Fácil  (2) Médio  (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        numero_de_tentativas = 20
    elif (nivel == 2):
        numero_de_tentativas = 10
    else:
        numero_de_tentativas = 5

    for rodada in range(1, numero_de_tentativas + 1):

        print("Tentativa {} de {}".format(rodada, numero_de_tentativas))
        chute_str = input("Digite seu chute: ")
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Seu chute deve estar entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou. Sua pontuação é de {}!".format(pontuacao))
            break
        else:
            if (maior):
                print("Você errou! O numero que você chutou é maior que o número secreto.")
            elif (menor):
                print("Você errou! O numero que você chutou é menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontuacao = pontuacao - pontos_perdidos
            if (numero_de_tentativas == rodada):
                print("O número secreto era {}. Você marcou {} pontos.".format(numero_secreto, pontos_perdidos))
    print("Fim do Jogo!")
    
if (__name__ == "__main__"):
    jogar()