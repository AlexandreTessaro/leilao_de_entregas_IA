import heapq
import itertools

def calcular_lucro_otimizado(destinos, matriz_conexoes, entregas):
    def custo_estimado(estado):
        if estado["entregas_restantes"]:
            max_bonus = max(e[2] for e in estado["entregas_restantes"])
        else:
            max_bonus = 0
        return -(estado["lucro"] + max_bonus)  

    estado_inicial = {
        "local_atual": "A",  
        "tempo_atual": 0,
        "lucro": 0,
        "entregas_restantes": entregas,
        "entregas_realizadas": []  
    }
    
    contador = itertools.count()
    
    fronteira = []
    heapq.heappush(fronteira, (custo_estimado(estado_inicial), len(estado_inicial["entregas_restantes"]), next(contador), estado_inicial))
    melhor_lucro = 0
    melhor_sequencia = []

    while fronteira:
        _, _, _, estado_atual = heapq.heappop(fronteira)

        local_atual = estado_atual["local_atual"]
        tempo_atual = estado_atual["tempo_atual"]
        lucro_atual = estado_atual["lucro"]
        entregas_restantes = estado_atual["entregas_restantes"]
        entregas_realizadas = estado_atual["entregas_realizadas"]

        if not entregas_restantes:
            if lucro_atual > melhor_lucro:
                melhor_lucro = lucro_atual
                melhor_sequencia = entregas_realizadas
            continue

        for entrega in entregas_restantes:
            tempo_inicio, destino, bonus = entrega
            idx_atual = destinos.index(local_atual)
            idx_destino = destinos.index(destino)

            tempo_deslocamento = matriz_conexoes[idx_atual][idx_destino]

            novo_tempo = tempo_atual + tempo_deslocamento

            if novo_tempo <= tempo_inicio:
                novo_estado = {
                    "local_atual": destino,
                    "tempo_atual": novo_tempo,  
                    "lucro": lucro_atual + bonus,  
                    "entregas_restantes": [e for e in entregas_restantes if e != entrega], 
                    "entregas_realizadas": entregas_realizadas + [(tempo_inicio, destino, bonus)]  
                }
                heapq.heappush(fronteira, (custo_estimado(novo_estado), len(novo_estado["entregas_restantes"]), next(contador), novo_estado))
            else:
                if lucro_atual > melhor_lucro:
                    melhor_lucro = lucro_atual
                    melhor_sequencia = entregas_realizadas

    return melhor_sequencia, melhor_lucro
