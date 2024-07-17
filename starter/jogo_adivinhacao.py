import random

numero_secreto = random.randint(1,10)
tentativas = 0

while True:
	tentativas += 1
	palpite = int(input("Adivinhe o número entre (1 e 10): "))
	
	if palpite < numero_secreto:
		print("Muito baixo")
	elif palpite > numero_secreto:
		print("Muito alto")
	else:
		print(f"Parabéns! Você acertou depois de {tentativas} tentativas.")
		break
