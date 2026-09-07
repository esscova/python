
# Trilha Python - Jornada de Dados
Instrutora: Luiza Vieira

## Seção 2 - Tipos e erros

### Temas
- Entendendo os tipos e erros
- Conversão de tipos e `input()`
- Tratamento de erros com `try/except`

### Exercícios

-  **Exercício 1 – Descobrindo os tipos**
	Observe os valores abaixo:  
	  
	nome = "Brasil"  
	gols = 3  
	posse_bola = 58.7  
	classificado = True  
	  
	Crie um programa que mostre o tipo de cada uma dessas variáveis utilizando `type()`.
	Ao executar, o programa deve permitir identificar quais valores são `str`, `int`, `float` e `bool`.

- **Exercício 2 – Verificando os tipos**

	Considere as variáveis:  
	  
	numero_camisa = 10  
	jogador = "Raphinha"  
	  
	Utilize `isinstance()` para verificar:
	  

	1.  se numero_camisa é um `int`;
	2.  se numero_camisa é uma `str`;
	3.  se jogador é uma `str`.

	Mostre o resultado de cada verificação na tela.

- **Exercício 3 – Encontre o Erro e Corrija**
	
	O código abaixo apresenta um erro:

	gols = "2"  
	novo_gol = gols + 1  
	  
	print(novo_gol)  
	 
	Execute o código, observe a mensagem apresentada pelo Python e responda:  

	-   Qual erro ocorreu?
	-   Quais são os tipos dos valores envolvidos?
	-   Por que esses valores não podem ser utilizados dessa forma?
	-   Corrija o programa para que o resultado exibido seja 3.

- **Exercício 5 – Convertendo valores decimais**

	Crie um programa que peça ao usuário:  
	  

	1.  o nome de um jogador;
	2.  sua nota na partida.

	  
	A nota pode possuir casas decimais, como 8.5.    
	Converta a nota para o tipo adequado e exiba uma mensagem semelhante a:
	  
	-   Vinicius recebeu a nota 8.5.
	  
	Antes de finalizar, utilize type() para verificar se a nota foi realmente convertida para o tipo esperado.

- **Exercício 6 – Quando precisamos de `str`**
	
	Considere:
	  
	numero = 10  
	jogador = "Rodrygo"  
	  
	Crie uma mensagem que resulte em:  
	
	-   O jogador Rodrygo veste a camisa 1.

	  
	Para este exercício, faça a construção da mensagem utilizando `+`.  
	Observe o erro que acontece ao tentar concatenar diretamente numero com os textos e depois utilize `str()` para corrigir o problema.  Explique por que a conversão foi necessária.

- **Exercício 7 – Deixando os valores explícitos**
	
	Crie as seguintes variáveis utilizando Type Hint:  
	
	-   nome da seleção → texto;
	-   quantidade de vitórias → número inteiro;
	-   aproveitamento → número decimal;
	-   seleção classificada → valor booleano.

	  
	Atribua um valor para cada variável.  
	Depois, altere propositalmente uma delas para um valor de outro tipo e observe o comportamento do Python.  

	Com base no que aconteceu, responda:   O Type Hint impede que uma variável receba outro tipo de valor durante a execução?

- **Exercício 8 – Impedindo o programa de quebrar**
	
	Crie um programa que pergunte a idade do usuário:  
	  
	Converta a resposta para `int`.  
	  
	Use `try/except` para impedir que o programa seja encerrado caso alguém digite algo como: _vinte_  
	  
	Se a conversão funcionar, mostre:

	1.  Idade registrada com sucesso.
	2.  Se ocorrer um `ValueError`, mostre:
	3.  Digite a idade utilizando apenas números.

- **Exercício 9 – Tratando entrada e validando o valor**  
  
	Uma avaliação de jogador deve receber uma nota entre 0 e 10.  
	  
	Crie um programa que peça essa nota ao usuário.  
	  
	O programa deve:    

	1.  tentar converter a entrada para `float`;
	2.  tratar um possível `ValueError`;
	3.  verificar se a nota está entre 0 e 10;
	4.  informar quando a nota estiver fora desse intervalo.
	  
	Exemplos:    
	
		Digite a nota: oito  
		Valor inválido. Digite um número.

		  
		Digite a nota: 15  
		A nota deve estar entre 0 e 10.

		  
		Digite a nota: 8.5  
		Nota registrada: 8.5

- **Exercício 10 – Continue perguntando até receber um valor válido**  
  
	Crie um programa para registrar a quantidade de gols de uma seleção.  O programa deve continuar perguntando:  _Quantos gols a seleção marcou?_ Até que o usuário forneça um número inteiro válido e maior ou igual a zero.  
	  
	Considere situações como:

		Quantos gols a seleção marcou? três

		Entrada inválida.

		  

		Quantos gols a seleção marcou? -2
	
		A quantidade de gols não pode ser negativa.

		  

		Quantos gols a seleção marcou? 4

		Quantidade de gols registrada: 4  
	  
	Para resolver o exercício, utilize os conteúdos estudados até aqui, incluindo:    

	-   `input()`;
	-   conversão com `int()`;
	-   `try/except`;
	-   `ValueError`;
	-   condição;
	-   `while`.

  
	O programa só deve parar de solicitar a informação quando receber um valor válido.
