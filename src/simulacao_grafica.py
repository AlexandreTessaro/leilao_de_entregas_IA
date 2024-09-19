import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from leilao_basico import calcular_lucro_basico
from leilao_otimizado import calcular_lucro_otimizado

def plotar_graficos(lucro_basico, lucro_otimizado):
    labels = ['Versão Básica', 'Versão Otimizada']
    lucros = [lucro_basico, lucro_otimizado]
    
    fig, ax1 = plt.subplots()

    ax1.bar(labels, lucros, color='blue', label='Lucro Obtido')
    ax1.set_ylabel('Lucro', color='blue')
    ax1.set_title('Comparação de Lucros entre Versões')

    plt.show()

def executar_simulacao():
    conexao_input = conexao_entry.get()
    entrega_input = entrega_entry.get()

    matriz_conexoes = np.array(eval(conexao_input))  
    entregas = eval(entrega_input)  

    destinos = ["A", "B", "C", "D"]  
    lucro_basico, _ = calcular_lucro_basico(destinos, matriz_conexoes, entregas)
    lucro_otimizado, _ = calcular_lucro_otimizado(destinos, matriz_conexoes, entregas)

    if isinstance(lucro_basico, list):
        lucro_basico = sum([bonus for _, _, bonus in lucro_basico]) 
    if isinstance(lucro_otimizado, list):
        lucro_otimizado = sum([bonus for _, _, bonus in lucro_otimizado])

    resultado_texto = f"Lucro esperado (básico): {lucro_basico}\nLucro esperado (otimizado): {lucro_otimizado}"
    messagebox.showinfo("Resultados", resultado_texto)

    plotar_graficos(lucro_basico, lucro_otimizado)

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
