"""
	SECAO 2 - TIPOS E ERROS
	EXERCICIO 04
	AUTOR: WELLINGTON M. SANTOS
	DATA: 2026-09-11
	OBJETIVO:
		- LEITURA DE DADOS
		- CONVERSÃO DE TIPOS
"""
print()
gols = input("Quantos gols a seleção marcou? ")

print('-'*30)
print(f'Tipo input: {type(gols)}')
gols = int(gols)
print(f'Tipo após conversão: {type(gols)}')
print('-'*30)

print(f'Com mais um gol a seleção terira {gols+1} gols.')