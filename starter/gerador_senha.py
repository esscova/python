from random import choice
import string

tam_senha = int(input("Quanto dígitos você quer na sua senha? "))
chars = string.ascii_letters + string.digits + string.punctuation

if tam_senha <= 0:
	print("A senha deve ser maior que 0")

else:
	senha = ''.join(choice(chars) for i in range(tam_senha))
	print("A senha gerada é:",senha)
