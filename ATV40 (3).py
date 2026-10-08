import random

sorteado = random.randint(1, 100)
tentativas = 0

print("Adivinhe o número sorteado entre 1 e 100!")

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite == sorteado:
        print(f"Parabéns, você acertou o número {sorteado} em {tentativas} tentativa(s)!")
        break
    elif palpite < sorteado:
        print("Errou! O número procurado é maior.")
    else:
        print("Errou! O número procurado é menor.")
