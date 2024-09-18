import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display
import numpy as np

# Função para calcular o lucro (pode ser o básico ou otimizado)
def calcular_lucro(destinos, conexoes, entregas):
    local_atual = "A"
    tempo_atual = 0
    lucro_total = 0
    entregas_realizadas = []

    for entrega in entregas:
        tempo_inicio, destino, bonus = entrega
        idx_atual = destinos.index(local_atual)
        idx_destino = destinos.index(destino)

        tempo_deslocamento = conexoes[idx_atual][idx_destino] * 2
        
        if tempo_atual + tempo_deslocamento <= tempo_inicio:
            lucro_total += bonus
            tempo_atual += tempo_deslocamento
            entregas_realizadas.append((tempo_inicio, destino, bonus))
            local_atual = destino
    
    return entregas_realizadas, lucro_total

# Função para atualizar o gráfico com base nos parâmetros ajustados
def atualizar_simulacao(bonus_B, bonus_C, bonus_D, tempo_inicio_B, tempo_inicio_C, tempo_inicio_D):
    destinos = ['A', 'B', 'C', 'D']
    conexoes = [
        [0, 5, 0, 2],
        [5, 0, 3, 0],
        [0, 3, 0, 8],
        [2, 0, 8, 0]
    ]

    entregas = [
        (tempo_inicio_B, 'B', bonus_B),
        (tempo_inicio_C, 'C', bonus_C),
        (tempo_inicio_D, 'D', bonus_D)
    ]

    entregas_realizadas, lucro = calcular_lucro(destinos, conexoes, entregas)

    # Limpar o gráfico anterior
    ax.clear()

    # Exibir as entregas realizadas
    tempos = [entrega[0] for entrega in entregas_realizadas]
    destinos_realizados = [entrega[1] for entrega in entregas_realizadas]
    lucros = [entrega[2] for entrega in entregas_realizadas]

    # Criar o gráfico
    ax.bar(destinos_realizados, lucros, color='blue')
    ax.set_xlabel('Destino')
    ax.set_ylabel('Bônus')
    ax.set_title(f'Lucro Total: {lucro}')

    # Redesenhar o gráfico
    plt.draw()

# Criar os controles interativos (sliders)
bonus_B_slider = widgets.IntSlider(value=1, min=0, max=20, step=1, description='Bônus B')
bonus_C_slider = widgets.IntSlider(value=10, min=0, max=20, step=1, description='Bônus C')
bonus_D_slider = widgets.IntSlider(value=8, min=0, max=20, step=1, description='Bônus D')

tempo_B_slider = widgets.IntSlider(value=0, min=0, max=20, step=1, description='Início B')
tempo_C_slider = widgets.IntSlider(value=5, min=0, max=20, step=1, description='Início C')
tempo_D_slider = widgets.IntSlider(value=10, min=0, max=20, step=1, description='Início D')

# Criar a área de plotagem
fig, ax = plt.subplots()

# Criar uma função de callback que será chamada sempre que os sliders forem modificados
widgets.interactive_output(atualizar_simulacao, {
    'bonus_B': bonus_B_slider,
    'bonus_C': bonus_C_slider,
    'bonus_D': bonus_D_slider,
    'tempo_inicio_B': tempo_B_slider,
    'tempo_inicio_C': tempo_C_slider,
    'tempo_inicio_D': tempo_D_slider
})

# Exibir os sliders e o gráfico
display(bonus_B_slider, bonus_C_slider, bonus_D_slider, tempo_B_slider, tempo_C_slider, tempo_D_slider)

# Mostrar o gráfico inicial
atualizar_simulacao(1, 10, 8, 0, 5, 10)
plt.show()
