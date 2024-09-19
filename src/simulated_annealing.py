import random
import math

def calcular_lucro_simulated_annealing(destinos, matriz_conexoes, entregas, temperatura_inicial=100, resfriamento=0.95, iteracoes=1000):
    def calcular_lucro(entregas_ordem):
        local_atual = "A"
        tempo_atual = 0
        lucro_total = 0
        entregas_realizadas = []

        for entrega in entregas_ordem:
            tempo_inicio, destino, bonus = entrega
            idx_atual = destinos.index(local_atual)
            idx_destino = destinos.index(destino)
            tempo_deslocamento = matriz_conexoes[idx_atual][idx_destino]

            if tempo_atual + tempo_deslocamento <= tempo_inicio:
                lucro_total += bonus
                tempo_atual += tempo_deslocamento
                entregas_realizadas.append((tempo_inicio, destino, bonus))
                local_atual = destino

        return entregas_realizadas, lucro_total

    def gerar_vizinho(entregas_ordem):
        nova_ordem = entregas_ordem[:]
        i, j = random.sample(range(len(nova_ordem)), 2)  
        nova_ordem[i], nova_ordem[j] = nova_ordem[j], nova_ordem[i]  
        return nova_ordem

    estado_atual = entregas[:]
    random.shuffle(estado_atual)  
    melhor_estado = estado_atual[:]
    melhor_lucro = calcular_lucro(melhor_estado)[1]

    temperatura = temperatura_inicial

    for _ in range(iteracoes):
        if temperatura <= 1:
            break

        novo_estado = gerar_vizinho(estado_atual)
        _, novo_lucro = calcular_lucro(novo_estado)
        _, lucro_atual = calcular_lucro(estado_atual)

        delta_lucro = novo_lucro - lucro_atual

        if delta_lucro > 0 or random.random() < math.exp(delta_lucro / temperatura):
            estado_atual = novo_estado

        if novo_lucro > melhor_lucro:
            melhor_estado = novo_estado
            melhor_lucro = novo_lucro

        temperatura *= resfriamento

    return melhor_estado, melhor_lucro
