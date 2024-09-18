import time
import matplotlib.pyplot as plt
from src.leilao_basico import calcular_lucro_basico
from src.leilao_otimizado import calcular_lucro_otimizado

def comparar_desempenho(destinos, matriz_conexoes, entregas):
    # Versão 1
    inicio_basico = time.time()
    lucro_basico = calcular_lucro_basico(destinos, matriz_conexoes, entregas)
    tempo_basico = time.time() - inicio_basico

    # Versão 2
    inicio_otimizado = time.time()
    lucro_otimizado = calcular_lucro_otimizado(destinos, matriz_conexoes, entregas)
    tempo_otimizado = time.time() - inicio_otimizado

    # Gráfico de Comparação
    labels = ['Versão Básica', 'Versão Otimizada']
    tempos = [tempo_basico, tempo_otimizado]
    lucros = [lucro_basico, lucro_otimizado]

    fig, ax1 = plt.subplots()

    ax1.bar(labels, tempos, color='blue', label='Tempo de Execução')
    ax1.set_xlabel('Versão')
    ax1.set_ylabel('Tempo (segundos)', color='blue')

    ax2 = ax1.twinx()
    ax2.plot(labels, lucros, color='red', marker='o', label='Lucro Obtido')
    ax2.set_ylabel('Lucro', color='red')

    plt.title('Comparação de Desempenho: Tempo vs Lucro')
    plt.show()
