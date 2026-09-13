"""
	SECAO 2 - TIPOS E ERROS
	EXERCICIO 02
	AUTOR: WELLINGTON M. SANTOS
	DATA: 2026-09-07
	OBJETIVO:
		- COMPREENSÃO DE TIPOS DE DADOS
		- UTILIZAÇÃO DO isintance()
"""

numero_camisa 	= 10
jogador			= 'Raphinha'

print(f"""

	VERIFICAÇÃO
	{'-'*50}

	Variável 'numero_camisa'
		- valor			 : {numero_camisa}
		- tipo 			 : {type(numero_camisa)}
		- instancia [int]: {isinstance(numero_camisa, int)}
		- instancia [str]: {isinstance(numero_camisa, str)}

	Variável 'jogador'
		- valor			 : {jogador}
		- tipo			 : {type(jogador)}
		- instancia [str]: {isinstance(jogador, str)}

	{'-'*50}
	
	""")