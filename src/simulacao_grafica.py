import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from leilao_basico import calcular_lucro_basico
from leilao_otimizado import calcular_lucro_otimizado
from simulated_annealing import calcular_lucro_simulated_annealing
from swarm import calcular_lucro_swarm

def plotar_graficos(lucro_basico, lucro_otimizado, lucro_sa, lucro_swarm):
    labels = ['Versão Básica', 'Versão Otimizada', 'Simulated Annealing', 'Swarm Optimization']
    lucros = [lucro_basico, lucro_otimizado, lucro_sa, lucro_swarm]
    
    fig, ax1 = plt.subplots()

    ax1.bar(labels, lucros, color='blue', label='Lucro Obtido')
    ax1.set_ylabel('Lucro', color='blue')
    ax1.set_title('Comparação de Lucros entre Versões')

    plt.show()

def executar_simulacao():
    conexao_input = conexao_entry.get()
    entrega_input = entrega_entry.get()

    # Fazer a cópia profunda da matriz de conexões e das entregas para garantir que cada algoritmo use seus próprios dados
    matriz_conexoes_original = np.array(eval(conexao_input))  
    entregas_original = eval(entrega_input)  

    destinos = ["A", "B", "C", "D"]  

    # Cópia profunda para cada algoritmo para garantir independência
    matriz_conexoes_basico = deepcopy(matriz_conexoes_original)
    entregas_basico = deepcopy(entregas_original)
    lucro_basico, _ = calcular_lucro_basico(destinos, matriz_conexoes_basico, entregas_basico)

    matriz_conexoes_otimizado = deepcopy(matriz_conexoes_original)
    entregas_otimizado = deepcopy(entregas_original)
    lucro_otimizado, _ = calcular_lucro_otimizado(destinos, matriz_conexoes_otimizado, entregas_otimizado)

    matriz_conexoes_sa = deepcopy(matriz_conexoes_original)
    entregas_sa = deepcopy(entregas_original)
    lucro_sa, _ = calcular_lucro_simulated_annealing(destinos, matriz_conexoes_sa, entregas_sa)

    matriz_conexoes_swarm = deepcopy(matriz_conexoes_original)
    entregas_swarm = deepcopy(entregas_original)
    lucro_swarm, _ = calcular_lucro_swarm(destinos, matriz_conexoes_swarm, entregas_swarm)

    # Somar os lucros corretamente se eles forem listas de entregas
    if isinstance(lucro_basico, list):
        lucro_basico = sum([bonus for _, _, bonus in lucro_basico]) 
    if isinstance(lucro_otimizado, list):
        lucro_otimizado = sum([bonus for _, _, bonus in lucro_otimizado])
    if isinstance(lucro_sa, list):
        lucro_sa = sum([bonus for _, _, bonus in lucro_sa])
    if isinstance(lucro_swarm, list):
        lucro_swarm = sum([bonus for _, _, bonus in lucro_swarm])

    resultado_texto = f"Lucro esperado (básico): {lucro_basico}\nLucro esperado (otimizado): {lucro_otimizado}\nLucro esperado (Simulated Annealing): {lucro_sa}\nLucro esperado (Swarm): {lucro_swarm}"
    messagebox.showinfo("Resultados", resultado_texto)

    # Plotar os gráficos de comparação
    plotar_graficos(lucro_basico, lucro_otimizado, lucro_sa, lucro_swarm)

root = tk.Tk()
root.title("Simulação Gráfica do Leilão de Entregas")

label_titulo = tk.Label(root, text="Simulação do Leilão de Entregas", font=("Arial", 16))
label_titulo.pack(pady=10)

conexao_label = tk.Label(root, text="Matriz de Conexões (Formato: [[0, 5, 0, 2], [5, 0, 3, 0], ...]):")
conexao_label.pack()
conexao_entry = tk.Entry(root, width=50)
conexao_entry.pack()

entrega_label = tk.Label(root, text="Lista de Entregas (Formato: [(0, 'B', 1), (5, 'C', 10), (10, 'D', 8)]):")
entrega_label.pack()
entrega_entry = tk.Entry(root, width=50)
entrega_entry.pack()

btn_executar = tk.Button(root, text="Executar Simulação", command=executar_simulacao, font=("Arial", 14))
btn_executar.pack(pady=20)

root.mainloop()
