"""
Exercicio 06
objetivo: pratica com match case
autor: Wellington M Santos
data: 2026-09-03
"""

posicao = input('Digite a posição do jogador [ goleiro | defesa | meio | ataque ]: ')

match posicao:
    case 'goleiro':
        print('Defende o gol.')
    case 'defesa':
        print('Impede o ataque do time adversário')
    case 'meio':
        print('Articula as jogadas entre a defesa e o ataque')
    case 'ataque':
        print('Finalização das jogadas ofensivas')
    case _:
        print('Posição inválida.')