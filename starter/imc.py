

peso = float(input("Digite seu peso em kg: ").replace(",","."))
altura = float(input("Digite sua altura em metros: ").replace(",","."))

imc = peso/(altura ** 2)

print(f"Seu IMC é: {imc:.2f}")
