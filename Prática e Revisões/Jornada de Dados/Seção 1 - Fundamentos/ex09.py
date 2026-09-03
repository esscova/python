"""
Exercicio 09
objetivo: pratica com estruturas de repetição
autor: Wellington M Santos
data: 2026-09-03
"""

print('Treino iniciado')
while True:
    continuar = input("Deseja realizar outro treino [ sim|nao ]: ")

    if continuar == 'nao':
        print('Treino encerrado.')
        break
    elif continuar == 'sim': print('Treino iniciado.')
    else: print('Responda por favor [sim ou nao]')