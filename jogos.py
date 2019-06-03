import adivinhacao
import forca

print("***********************************************")
print("*                                             *")
print("*              Escolha seu Jogo               *")
print("*                                             *")
print("***********************************************")


print("(1) Adivinhação  (2) Forca")
jogo = int(input("Digite o número do jogo: "))
if (jogo == 1):
    adivinhacao.jogar()
else:
    forca.jogar()


