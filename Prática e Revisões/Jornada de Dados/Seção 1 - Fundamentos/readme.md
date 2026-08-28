
# Seção 1 - Fundamentos

Instrutora: Luiza Vieira


### Temas

- Variáveis e tipos de dados
- Booleanos e operados
- Estruturas de decisão
- Estruturas de repetição

### Exercícios

1. **Exercício 1 – Criando suas primeiras variáveis**  
  
    Crie um programa para armazenar algumas informações sobre uma seleção:   
    1.  nome da seleção;
    2.  quantidade de títulos;
    3.  posição no ranking;
    4.  se está classificada para a Copa. 

    Ao final, imprima todos os valores na tela.

2. **Exercício 2 – Calculando o placar**  
  
    Uma seleção marcou 3 gols no primeiro tempo e 2 gols no segundo tempo.  
    
    Crie variáveis para armazenar essas duas informações e calcule:  

    1.  o total de gols da partida;
    2.  quantos gols foram marcados a mais no primeiro tempo em relação ao segundo.

    
    Ao final, imprima os resultados na tela.

3. **Exercício 3 – Trabalhando com operadores**  
  
    Considere:
    
    pontos = 7  
    vitorias = 2  
    saldo_gols = 4  
    
    Crie expressões que respondam às seguintes perguntas: 


    1.  A seleção possui mais de 5 pontos?
    2.  A seleção possui exatamente 3 vitórias?
    3.  O saldo de gols é maior ou igual a 0?
    4.  A seleção possui mais de 5 pontos e saldo de gols positivo?
    5.  A seleção possui 3 vitórias ou mais de 6 pontos?

    
    Mostre o resultado de cada expressão.

4. **Exercício 4 – Seleção classificada ou eliminada?**  
  
    Crie uma variável chamada pontos e atribua a ela uma quantidade de pontos.  
    
    Depois, utilizando `if` e `else`, faça o programa mostrar: "Seleção classificada!"  
    caso tenha 6 pontos ou mais.  
    
    Caso contrário, mostre:  "Seleção eliminada."  
    
    Teste o programa alterando manualmente o valor da variável para verificar os dois caminhos.

5. **Exercício 5 – Avaliando o desempenho da seleção**  

    Crie uma variável chamada pontos.  
    
    Utilizando `if, elif` e `else`, classifique o desempenho da seleção da seguinte forma:  

    -   7 pontos ou mais → Excelente campanha
    -   de 4 a 6 pontos → Campanha regular
    -   menos de 4 pontos → Campanha ruim

    
    Teste o programa utilizando diferentes valores para pontos.

6. **Exercício 6 – Posição do jogador**  

    Utilizando o `input()`, peça ao usuário para informar a posição de um jogador. As opções esperadas são:


    1.  goleiro
    2.  defesa
    3.  meio
    4.  ataque

    Armazene a resposta em uma variável chamada posicao.
    
    Depois, utilize `match case` para verificar a posição informada e mostrar uma mensagem correspondente à função daquele jogador em campo.  
    
    Por exemplo:  _Digite a posição do jogador: ataque_  
    
    Saída esperada: Responsável principalmente pela criação e finalização das jogadas ofensivas.  
    
    Crie também um caso para quando o usuário digitar uma posição diferente das opções esperadas. Nesse caso, mostre: Posição inválida.

7. **Exercício 7 – Simulando as cinco cobranças de pênalti**  
    Uma disputa de pênaltis começa com cinco cobranças para uma equipe.  
    
    Utilize for e `range()` para mostrar na tela:
    

    -   Cobrança 1
    -   Cobrança 2
    -   Cobrança 3
    -   Cobrança 4
    -   Cobrança 5

    Depois das cinco repetições, mostre: "Fim das cobranças iniciais."

8. **Exercício 8 – Contando gols**  

    Crie uma variável: gols = 0  
    
    Depois, utilize um `for` para simular 5 oportunidades de gol.
    
    A cada repetição, acrescente 1 à variável gols e mostre a quantidade atual.    
    O resultado deve seguir esta ideia:  

    -   Gol! Total: 1
    -   Gol! Total: 2
    -   Gol! Total: 3
    -   ...

    Ao final, mostre a quantidade total de gols.

9. **Exercício 9 – Continue até o usuário decidir parar**  

    Crie um programa que permaneça em execução enquanto o usuário responder: "sim"  
    
    A cada repetição, mostre: "Treino iniciado!"  
    Depois, pergunte novamente: "Deseja realizar outro treino?"  
    
    Quando a resposta for diferente de  _sim_, o `while` deve terminar e o programa deve mostrar: "Treino encerrado."  
    Não é necessário trabalhar com números neste exercício. Utilize a resposta do `input()` como texto.

10. **Exercício 10 – Simulando uma sequência de cobranças**  

    Crie um pequeno programa para representar uma disputa de cinco pênaltis.  

    Para cada cobrança, o programa deve perguntar ao usuário: "Resultado da cobrança: gol ou perdeu?"  
    
    Utilize um `for` para garantir que sejam realizadas exatamente 5 cobranças.  
    
    A cada resposta:

    -   se for gol, aumente o contador de gols em 1;
    -   se for perdeu, não aumente o contador;
    -   se for qualquer outro valor, mostre que a opção informada não foi reconhecida.

    Ao final das cinco cobranças:    

    -   se a seleção tiver marcado 4 ou 5 gols, mostre: "Ótimo desempenho nos pênaltis!";
    -   se tiver marcado 2 ou 3, mostre: "Desempenho regular nos pênaltis.";
    -   se tiver marcado 0 ou 1, mostre: "Desempenho ruim nos pênaltis."

    Por fim, mostre também a quantidade total de gols marcados.    
    Para resolver esta questão, combine conteúdos estudados ao longo do módulo, como:  
    -   variáveis;
    -   valores booleanos e comparações;
    -   `input()`;
    -   `if, elif` e `else`;
    -   `for`;
    -   contador com `+=`.
