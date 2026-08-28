"""
Exercicio 03
objetivo: pratica com operadores logicos
autor: Wellington M Santos
data: 2026-08-28
"""

pontos      = 7
vitorias    = 2
saldo_gols  = 4

print()
print(f'A seleção possui mais de 5 pontos?                          : {pontos>5}')
print(f'A seleção possui exatamente 3 vitórias?                     : {vitorias == 3}')
print(f'O saldo de gols é maior ou igual a 0?                       : {saldo_gols>=0}')
print(f'A seleção possui mais de 5 pontos e saldo de gols positivo? : {(pontos>5 and saldo_gols>0)}')
print(f'A seleção possui 3 vitórias ou mais de 6 pontos?            : {(vitorias == 3 or pontos>6)}')
print()