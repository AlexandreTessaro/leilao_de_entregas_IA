import numpy as np
import random

class Particula:
    def __init__(self, destinos, entregas):
        self.posicao = random.sample(entregas, len(entregas))  
        self.velocidade = [0] * len(entregas)
        self.melhor_posicao = list(self.posicao)
        self.melhor_lucro = -float('inf')

    def calcular_lucro(self, destinos, matriz_conexoes):
        local_atual = "A"
        tempo_atual = 0
        lucro_total = 0
        entregas_realizadas = set()  

        for entrega in self.posicao:
            tempo_inicio, destino, bonus = entrega
            idx_atual = destinos.index(local_atual)
            idx_destino = destinos.index(destino)

            tempo_deslocamento = matriz_conexoes[idx_atual][idx_destino]

            if tempo_atual + tempo_deslocamento <= tempo_inicio and destino not in entregas_realizadas:
                lucro_total += bonus
                tempo_atual += tempo_deslocamento
                local_atual = destino
                entregas_realizadas.add(destino) 

        return lucro_total

    def atualizar_velocidade(self, melhor_global, w=0.5, c1=1.5, c2=1.5):
        for i in range(len(self.velocidade)):
            r1 = random.random()
            r2 = random.random()

            if melhor_global: 
                self.velocidade[i] = (
                    w * self.velocidade[i] +
                    c1 * r1 * (self.melhor_posicao[i][2] - self.posicao[i][2]) +
                    c2 * r2 * (melhor_global[i][2] - self.posicao[i][2])
                )
            else:
                self.velocidade[i] = w * self.velocidade[i]  

    def atualizar_posicao(self, destinos, matriz_conexoes):
        for i in range(len(self.posicao)):
            self.posicao[i] = random.choice(self.posicao) if random.random() < abs(self.velocidade[i]) else self.posicao[i]

        lucro_atual = self.calcular_lucro(destinos, matriz_conexoes)

        if lucro_atual > self.melhor_lucro:
            self.melhor_posicao = list(self.posicao)
            self.melhor_lucro = lucro_atual


def calcular_lucro_swarm(destinos, matriz_conexoes, entregas, num_particulas=30, iteracoes=100):
    enxame = [Particula(destinos, entregas) for _ in range(num_particulas)]
    melhor_global = None
    melhor_lucro_global = -float('inf')

    for _ in range(iteracoes):
        for particula in enxame:
            particula.atualizar_velocidade(melhor_global)
            particula.atualizar_posicao(destinos, matriz_conexoes)

            if particula.melhor_lucro > melhor_lucro_global:
                melhor_lucro_global = particula.melhor_lucro
                melhor_global = list(particula.melhor_posicao)

    return melhor_global, melhor_lucro_global
