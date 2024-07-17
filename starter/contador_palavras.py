
def contador_palavras(texto):
	palavras = texto.split()
	contagem = {}

	for palavra in palavras:
		if palavra in contagem:
			contagem[palavra] += 1
		else:
			contagem[palavra] = 1

	return contagem

texto = input('Digite um texto: ')
contagem = contador_palavras(texto)

for i, j in contagem.items():
	print(f'{i} : {j}')
