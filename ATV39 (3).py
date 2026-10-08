import random

sorteado = random.randint(1, 10)
palpite = int(input("Tente adivinhar o número sorteado entre 1 e 10: "))

if palpite == sorteado:
    print(f"Parabéns, você acertou! O número era {sorteado}.")
else:
    print(f"Você errou, o número sorteado era {sorteado}.")
