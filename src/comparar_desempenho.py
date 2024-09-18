import time
import matplotlib.pyplot as plt
from src.leilao_basico import calcular_lucro_basico
from src.leilao_otimizado import calcular_lucro_otimizado

def comparar_desempenho(destinos, conexoes, entregas):
    # Exemplo básico para comparar desempenho
    print("\nComparando desempenho...")

    # Medir desempenho da versão básica
    inicio_basico = time.time()
    _, lucro_basico = calcular_lucro_basico(destinos, conexoes, entregas)  # Pegamos apenas o lucro
    tempo_basico = time.time() - inicio_basico

    # Medir desempenho da versão otimizada
    inicio_otimizado = time.time()
    _, lucro_otimizado = calcular_lucro_otimizado(destinos, conexoes, entregas)  # Pegamos apenas o lucro
    tempo_otimizado = time.time() - inicio_otimizado

    # Preparar os dados para o gráfico
    labels = ['Básico', 'Otimizado']
    tempos = [tempo_basico, tempo_otimizado]
    lucros = [lucro_basico, lucro_otimizado]  # Certificar que os lucros são valores numéricos

    # Gráfico de comparação de desempenho
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Versão')
    ax1.set_ylabel('Tempo de Execução (s)', color='blue')
    ax1.bar(labels, tempos, color='blue', alpha=0.6, label='Tempo de Execução')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Lucro Obtido', color='red')
    ax2.plot(labels, lucros, color='red', marker='o', label='Lucro Obtido')

    fig.tight_layout()
    plt.title('Comparação de Desempenho')
    plt.show()

    print(f"Tempo versão básica: {tempo_basico:.5f}s, lucro: {lucro_basico}")
    print(f"Tempo versão otimizada: {tempo_otimizado:.5f}s, lucro: {lucro_otimizado}")
