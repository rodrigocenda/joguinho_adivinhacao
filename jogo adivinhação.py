import random

numero=(random.randrange(1,101))
rodada=1
pontos=1000
print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if (nivel == 1):
    tentativas=15
elif (nivel == 2):
    tentativas=10
else:
    tentativas=5


for rodada in range(1, tentativas+1):
    print("Tentativa {} de {}".format(rodada, tentativas))
    chute=int(input("adivinhe o número de 1-100: "))
    if chute>100 or chute<0:
        print("de 1-100 só")
        continue
    else:
        if (chute==numero):
            print("voce acertou \n pontos: {} \n número: {} \n\n parabens".format(pontos, numero))
            break
        else:
            if chute<numero:
                print("maior")
                if (rodada == tentativas):
                    print("O número secreto era {}. Você fez {} pontos".format(numero, pontos))
            else:
                print('menor')
                if (rodada == tentativas):
                    print("O número secreto era {}. Você fez {} pontos".format(numero, pontos))
            pontos_perdidos=abs(numero-chute)
            pontos=pontos-pontos_perdidos
