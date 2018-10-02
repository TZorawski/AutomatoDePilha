# Autômato de Pilha
Este repositório contém a implementação de um programa desenvolvido em Python que simula a execução de autômatos de pilha não-determinísticas.

### Introdução
O programa foi desenvolvido por Vitor Bueno, Thaís Zorawski, Cláudia Sampedro e Lucas Ribeiro, alunos do curso Bacharelado em Ciência da Computação da Universidade Tecnológica Federal do Paraná – *câmpus* Campo Mourão (UTFPR-CM). Tal programa foi desenvolvido no semestre 2018/2, para a disciplina Linguagens Formais, Autômatos e Computabilidade, ministrada pelo professor Marco Aurélio Graciotto Silva, do Departamento de Computação da UTFPR-CM (DACOM).

### Sobre o Autômato de Pilha
Um *Autômato de Pilha* é um modelo teórico parecido com o funcionameto de máquinas de Turing. Uma MT é uma máquina que manipula símbolos em uma fita, de acordo com um conjunto de regras e transições. Assim como uma máquina de Turing, um Autômato de Pilha possui um alfabeto, que será o conjunto de símbolos aceitáveis pelo autômato, um conjunto de estados possíveis, uma palavra de entrada, uma pilha e um conjunto de transições que indicam o que acontecerá com a autômato e com a pilha de acordo com o valor que é lido na entrada do autômato.

### Execução do programa
- Este programa é uma adaptação de um programa que foi desenvolvido anteriormente pelos mesmos alunos e está disponível [neste link](https://github.com/claudiaps/TuringMachine). Sendo assim, este programa está dividido em dois arquivos: ***main.py*** e ***automato_pilha.py***. O arquivo *main.py* é responsável por ler o arquivo texto que contém o autômato, ler a palavra de entrada e chamar a execução do arquivo *automato_pilha.py* que contém toda a lógica de funcionamento de um Autômato de Pilha. ***Falar sobre a implementação...***

- O formato de instrução para execução do programa é:  
	    `python main.py “automato.txt” “entrada”`
    
  **Exemplo:**  
  `python main.py exemplos/ww^r.txt aabbaa`

- Para testes, no diretório *"exemplos"* deste repositório existem alguns exemplos de arquivos com Autômatos de Pilha no formato que deve ser usado como entrada para o programa.

- O formato de saída do programa é:  
  `{'word', 'current_state', 'stack'}`

  Em que, *‘word’* indica o conteúdo final da palavra de entrada, *‘current_state’* indica o estado no qual o autômato se encontra ao final da execução e  *‘stack’* indica o conteúdo final da pilha.
  
  Além disso, na saída do programa haverá uma linha indicando o resultado final de execução do Autômato, podendo ser:
  `0: Computação terminada e aceita.`  
  `-1: Computação terminada e rejeitada.`  
  `-3: Valor inserido na palavra incorreto`  
  `-4: Epsilon inválido`

  **Exemplo de Saída:**  
  `0: Computação terminada e aceita.`  
  `{'word': '', 'current_state': 'q2', 'stack': []}`
  
- Para converter Autômatos de Pilha do formato *.jff* para *.txt* (formato aceito pelo programa), use o arquivo *jflap-pda2utfpr.py*, da seguinte forma:

  `python jflap-pda2utfpr.py pda.jff pda.txt`
  
### Considerações Finais
Com o desenvolvimento deste programa, os autores puderam compreender afundo o funcionamento e propósito geral dos Autômatos de Pilha.

  
