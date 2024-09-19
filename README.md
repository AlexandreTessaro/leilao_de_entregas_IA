# Projeto: Leilão de Entregas

## Descrição

Este projeto tem como objetivo desenvolver uma solução para o problema do **Leilão de Entregas**, onde uma empresa de logística precisa maximizar o lucro selecionando as entregas de forma otimizada. Os clientes oferecem bônus para priorizar suas entregas, e a missão da empresa é organizar as entregas diárias de maneira eficiente, tanto no modo básico quanto no modo otimizado usando técnicas de inteligência artificial.

## Funcionalidades

O projeto implementa duas versões para resolver o problema:

1.  **Versão Básica**: Um algoritmo simples que processa a lista de entregas sequencialmente, sem otimizações.
2.  **Versão Otimizada**: Um algoritmo que utiliza técnicas de otimização para encontrar a sequência de entregas que maximiza o lucro.

## Estrutura do Projeto


    n1---claudiuNey/
    │
    ├── data/
    │   ├── conexoes.txt        # Matriz de conexões entre os destinos
    │   └── entregas.txt        # Lista de entregas, horários, destinos e bônus
    ├── src/
    │   ├── comparar_desempenho.py  # Script que compara o desempenho das duas versões
    │   ├── leilao_basico.py        # Algoritmo básico do leilão de entregas
    │   ├── leilao_otimizado.py     # Algoritmo otimizado do leilão de entregas
    │   ├── leitura_dados.py        # Funções para ler a matriz de conexões e a lista de entregas
    │   └── simulacao_grafica.py    # Interface gráfica para rodar a simulação
    ├── main.py                  # Arquivo principal que executa o projeto
    └── README.md                # Documentação do projeto

## Como Executar

### Pré-requisitos

Certifique-se de ter o Python 3 instalado em sua máquina. Além disso, instale as dependências necessárias executando o seguinte comando na raiz do projeto:

`pip install -r requirements.txt` 

### Execução

1.  **Executar a Versão Básica e Otimizada**: Para executar o projeto e comparar o desempenho das versões, use o comando:
    
    
    `python main.py` 
    
2.  **Executar a Simulação Gráfica**: Caso queira rodar a simulação gráfica, execute o seguinte comando:
  
    
    `python src/simulacao_grafica.py` 
    

## Formato dos Arquivos de Entrada

### `conexoes.txt`

Este arquivo contém a matriz de conexões entre os destinos. A primeira linha contém os nomes dos destinos, e as linhas subsequentes contêm os tempos de deslocamento entre os destinos.

Exemplo de formato:



    A, B, C, D
    0, 5, 0, 2
    5, 0, 3, 0
    0, 3, 0, 8
    2, 0, 8, 0

### `entregas.txt`

Este arquivo contém as entregas programadas, com o tempo de início, o destino, e o bônus oferecido.

Exemplo de formato:



    0, B, 1
    5, C, 10
    10, D, 8

## Comparação de Desempenho

O projeto inclui uma função que compara o desempenho das versões básica e otimizada. Ele exibe o **lucro** e o **tempo de execução** de cada versão, e gera gráficos comparativos usando a biblioteca `matplotlib`.

## Tecnologias Utilizadas

-   **Python 3.x**
-   **Bibliotecas**:
    -   `numpy` para manipulação de arrays e matrizes de conexões.
    -   `heapq` para a implementação da otimização de prioridade.
    -   `matplotlib` para geração de gráficos comparativos.
    -   `tkinter` para interface gráfica (simulação).

## Autores

Este projeto foi desenvolvido por:

-   [Alexandre Tessaro Vieira](https://github.com/AlexandreTessaro) – Desenvolvedor 
-   [Richard Schmitz](https://github.com/AlexandreTessaro) – Desenvolvedor 
-   [Leonardo Pereira](https://github.com/AlexandreTessaro) – Desenvolvedor  
-   [Wuelliton Christian](https://github.com/AlexandreTessaro) – Desenvolvedor
-   [Edson Borges](https://github.com/AlexandreTessaro) – Desenvolvedor  

----------



