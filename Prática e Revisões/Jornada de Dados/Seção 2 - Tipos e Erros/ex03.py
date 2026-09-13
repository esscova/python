"""
	SECAO 2 - TIPOS E ERROS
	EXERCICIO 03
	AUTOR: WELLINGTON M. SANTOS
	DATA: 2026-09-07
	OBJETIVO:
		- COMPREENSÃO DE TIPOS DE ERROS
		- HÁBITO DE LEITURA E COMPREENSÃO DE ERROS
"""

gols 	 = '2'

if isinstance(gols, int):
	novo_gol = gols + 1
	print(novo_gol)
else:
	print(f'Tipo atual gols: {type(gols)}')
	print('Convertendo tipo...')
	novo_gol = int(gols) + 1
	print(f'Valor da operação após conversão:: {novo_gol}')