"""
    SECAO 2 - TIPOS E ERROS
    EXERCICIO 07
    AUTOR: WELLINGTON M. SANTOS
    DATA: 2026-09-11
    OBJETIVO:
        - 
"""

nome_da_selecao:str         = 'quirguistão'
quantidade_de_vitorias:int  = 10
aproveitamento:float        = 100.0
selecao_classificada:bool   = True
teste_type_hint:bool        = 'O Type Hint não impede que uma variável receba outro tipo de valor durante a execução.'

print(f"""

    RELATORIO
    ------------------------
    - SELEÇÃO : {nome_da_selecao}
    - VITORIAS: {quantidade_de_vitorias}
    - APROVEITAMENTO: {aproveitamento} %
    - CLASSIFICADA  : {'SIM' if selecao_classificada else 'NÂO'}
    ------------------------

    Nota de uso do Type Hint: {teste_type_hint} \n
""")