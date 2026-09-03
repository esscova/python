"""
Exercicio 10
objetivo: pratica com estruturas de repetição e decisão
autor: Wellington M Santos
data: 2026-09-03
"""

cobrancas   = 5
gols        = 0

for i in range(cobrancas):
    while True:
        resultado   = input("Resultado da cobrança [ gol | perdeu ]: ")
        if resultado == 'gol':
            gols += 1
            break
        elif resultado == 'perdeu': break
        else: print("A opção informada não foi reconhecida.")

if gols >= 4   :print('Ótimo desempenho nos pênaltis.')
elif gols >= 2 :print('Desempenho regular nos pênaltis')
else           :print('Desempenho ruim nos pênaltis')

print(f'Total de gols marcados: {gols}')