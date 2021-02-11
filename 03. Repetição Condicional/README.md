<div id='topo'/>

# Repetição Condicional

Enunciado dos Exercícios:

 * [Rep. Cond. 1) Somador](#RepCond1)
 * [Rep. Cond. 2) Médias](#RepCond2)
 * [Rep. Cond. 3) Somador 2](#RepCond3)
 * [Rep. Cond. 4) PokemonGo](#RepCond4)
 * [Rep. Cond. 5) Ordem](#RepCond5)
 * [Rep. Cond. 6) Pedra Papel Tesoura e mais](#RepCond6)

*******

<div id='RepCond1'/>

## Rep. Cond. 1) Somador

Faça um programa que receba números inteiros e calcule a soma desses números, até que seja fornecido o número 0.

* ### Entrada:

  Números inteiros.

* ### Saída:

  Número inteiro representando a soma dos números informados.  

###### Resposta: [RepCond1.py](https://github.com/biancamendes/Computer-Programming-Exercises-PT-BR-/blob/main/03.%20Repeti%C3%A7%C3%A3o%20Condicional/RepCond1.py)
###### [Topo](#topo)
  
*******

<div id='RepCond2'/>

## Rep. Cond. 2) Médias

Faça um programa que irá somar a média de X alunos. O programa recebe primeiro um número X de alunos, e para cada um desses alunos, irá receber 2 notas, onde a média dessas duas notas será somada (para cada aluno) e apresentada no final a soma das médias dos X alunos.

* ### Entrada:

  Número X (inteiro) de alunos, seguido por 2X notas (reais) representando as notas dos alunos.

* ### Saída:

  Número (real com 2 casas decimais) representando a soma das médias.  

###### Resposta: [RepCond2.py](https://github.com/biancamendes/Computer-Programming-Exercises-PT-BR-/blob/main/03.%20Repeti%C3%A7%C3%A3o%20Condicional/RepCond2.py)
###### [Topo](#topo)
  
*******

<div id='RepCond3'/>

## Rep. Cond. 3) Somador 2

Faça um programa que receba números inteiros e calcule a soma desses números, até que seja fornecido novamente o primeiro número fornecido desta soma. Neste caso o programa soma novamente este primeiro número, para, e imprime a soma.

* ### Entrada:

  Números inteiros.

* ### Saída:

  Número inteiro representando a soma dos números informados.  

###### Resposta: [RepCond3.py](https://github.com/biancamendes/Computer-Programming-Exercises-PT-BR-/blob/main/03.%20Repeti%C3%A7%C3%A3o%20Condicional/RepCond3.py)
###### [Topo](#topo)
  
*******

<div id='RepCond4'/>

## Rep. Cond. 4) PokemonGo

Suponha que um jogador A de PokemonGO tenha X pokemons com uma taxa anual de crescimento/captura de 50% e que o jogador B tem Y pokemons com uma taxa de crescimento/captura de 30%.

Vamos assumir que (pode acreditar):

* X < Y
* X >= 2
* A quantidade de pokemons capturada por ano é inteira, que dizer, por exemplo, se eu tenho 123 pokemons e tenho uma taxa de captura de 30% no ano, então em um ano ireicapturar 47 pokemons pois 30% de 123 é 47.70 (pegamos só a parte inteira ou piso).

Faça um programa que calcule e retorne o número de anos necessários para que o jogador A ultrapasse ou iguale o número de pokemons do jogador B, mantidas as taxas de crescimento

* ### Entrada:

  Números inteiros X e Y indicando o número inicial de pokemons do jogador A e B respectivamente.

* ### Saída:

  Número de anos (inteiro) para que A ultrapasse ou iguale B.  

###### Resposta: [RepCond4.py](https://github.com/biancamendes/Computer-Programming-Exercises-PT-BR-/blob/main/03.%20Repeti%C3%A7%C3%A3o%20Condicional/RepCond4.py)
###### [Topo](#topo)
  
*******

<div id='RepCond5'/>

## Rep. Cond. 5) Ordem

Fazer um programa que lê N números inteiros do teclado, e no final informa se os números lidos estão ou não em ordem crescente.

Vamos assumir que (pode acreditar):

* N >= 2

**Dica**: guarde sempre o número anterior fornecido.

* ### Entrada:

  Número inteiro N, seguido de N números inteiros.

* ### Saída:

  `sim` se os números estão em ordem crescente e `não` caso contrário.  

###### Resposta: [RepCond5.py](https://github.com/biancamendes/Computer-Programming-Exercises-PT-BR-/blob/main/03.%20Repeti%C3%A7%C3%A3o%20Condicional/RepCond5.py)
###### [Topo](#topo)
  
*******

<div id='RepCond6'/>

## Rep. Cond. 6) Pedra Papel Tesoura e mais

Faça um jogo de pedra, papel, tesoura, spock e lagarto (de onde vem isso?), onde dois jogadores escolhem entre “0-pedra 1-spock 2-paper 3-lagarto 4-tesoura”. Serão disputadas 3 partidas e o programa deve informar quantas vezes cada jogador ganhou e quantas vezes deu empate.

A ordem de vitória:

![](https://github.com/biancamendes/Computer-Programming-Exercises-PT-BR-/blob/main/03.%20Repeti%C3%A7%C3%A3o%20Condicional/RepCond6.IMG.jpg)  

* ### Entrada:

  6 números (inteiros) representando as jogadas alternadas dos jogadores 1 e 2, isto é, o primeiro número é a jogada 1 do jogador 1, o segundo número é a jogada 1 do jogador 2, e assim por diante.

* ### Saída:

  3 números inteiros (um em cada linha) indicando o número de vitórias do jogador 1, o número de vitórias do jogador 2 e o número de empates.  

###### Resposta: [RepCond6.py](https://github.com/biancamendes/Computer-Programming-Exercises-PT-BR-/blob/main/03.%20Repeti%C3%A7%C3%A3o%20Condicional/RepCond6.py)
###### [Topo](#topo)
