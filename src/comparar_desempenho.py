import time
import matplotlib.pyplot as plt
from src.leilao_basico import calcular_lucro_basico
from src.leilao_otimizado import calcular_lucro_otimizado
from src.simulated_annealing import calcular_lucro_simulated_annealing  
from src.swarm import calcular_lucro_swarm  

def comparar_desempenho(destinos, conexoes, entregas):
    print("\nComparando desempenho...")

    inicio_basico = time.perf_counter()
    _, lucro_basico = calcular_lucro_basico(destinos, conexoes, entregas)
    tempo_basico = (time.perf_counter() - inicio_basico) * 10000  

    inicio_otimizado = time.perf_counter()
    _, lucro_otimizado = calcular_lucro_otimizado(destinos, conexoes, entregas)
    tempo_otimizado = (time.perf_counter() - inicio_otimizado) * 10000  

    inicio_sa = time.perf_counter()
    _, lucro_sa = calcular_lucro_simulated_annealing(destinos, conexoes, entregas)
    tempo_sa = (time.perf_counter() - inicio_sa) * 10000  

    inicio_swarm = time.perf_counter()
    _, lucro_swarm = calcular_lucro_swarm(destinos, conexoes, entregas)
    tempo_swarm = (time.perf_counter() - inicio_swarm) * 10000 

    labels = ['Básico', 'Otimizado', 'Simulated Annealing', 'Swarm Optimization']
    lucros = [lucro_basico, lucro_otimizado, lucro_sa, lucro_swarm]
    tempos = [tempo_basico, tempo_otimizado, tempo_sa, tempo_swarm]

    fig1, ax1 = plt.subplots()
    ax1.set_xlabel('Versão')
    ax1.set_ylabel('Lucro Obtido', color='black')
    bars_lucro = ax1.bar(labels, lucros, color='grey', alpha=0.6, label='Lucro Obtido')

    for bar, lucro in zip(bars_lucro, lucros):
        ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                 f'{lucro}', ha='center', va='bottom', color='black')

    plt.title('Comparação de Lucros')
    plt.show()

    fig2, ax2 = plt.subplots()
    ax2.set_xlabel('Versão')
    ax2.set_ylabel('Tempo de Execução (ms)', color='blue')
    bars_tempo = ax2.bar(labels, tempos, color='blue', alpha=0.6, label='Tempo de Execução')

    for bar, tempo in zip(bars_tempo, tempos):
        ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                 f'{tempo:.2f}ms', ha='center', va='bottom', color='black')

    plt.title('Comparação de Tempos de Execução')
    plt.show()

    print(f"Lucro versão básica: {lucro_basico}, Tempo: {tempo_basico:.5f}ms")
    print(f"Lucro versão otimizada: {lucro_otimizado}, Tempo: {tempo_otimizado:.5f}ms")
    print(f"Lucro versão Simulated Annealing: {lucro_sa}, Tempo: {tempo_sa:.5f}ms")
    print(f"Lucro versão Swarm Optimization: {lucro_swarm}, Tempo: {tempo_swarm:.5f}ms")
