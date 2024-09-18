import heapq
import itertools

def calcular_lucro_otimizado(destinos, matriz_conexoes, entregas):
    # Função para estimar o custo do estado atual, usando uma heurística baseada nos maiores bônus
    def custo_estimado(estado):
        # Estimativa heurística: lucro atual mais o maior bônus disponível nas entregas restantes
        if estado["entregas_restantes"]:
            max_bonus = max(e[2] for e in estado["entregas_restantes"])
        else:
            max_bonus = 0
        return -(estado["lucro"] + max_bonus)  # Negativo porque heapq é uma min-heap

    # Estado inicial
    estado_inicial = {
        "local_atual": "A",  # Sempre começando no ponto A
        "tempo_atual": 0,
        "lucro": 0,
        "entregas_restantes": entregas,
        "entregas_realizadas": []  # Para rastrear a sequência de entregas
    }
    
    # Cria um contador para garantir que os estados sejam únicos e possam ser comparados
    contador = itertools.count()
    
    fronteira = []
    # Usar apenas o custo estimado como o critério de comparação
    heapq.heappush(fronteira, (custo_estimado(estado_inicial), len(estado_inicial["entregas_restantes"]), next(contador), estado_inicial))
    melhor_lucro = 0
    melhor_sequencia = []

    while fronteira:
        # Pegamos o estado com menor custo estimado
        _, _, _, estado_atual = heapq.heappop(fronteira)

        local_atual = estado_atual["local_atual"]
        tempo_atual = estado_atual["tempo_atual"]
        lucro_atual = estado_atual["lucro"]
        entregas_restantes = estado_atual["entregas_restantes"]
        entregas_realizadas = estado_atual["entregas_realizadas"]

        # Se não há mais entregas restantes, atualiza o melhor lucro e a melhor sequência de entregas
        if not entregas_restantes:
            if lucro_atual > melhor_lucro:
                melhor_lucro = lucro_atual
                melhor_sequencia = entregas_realizadas
            continue

        # Testa cada entrega possível
        for entrega in entregas_restantes:
            tempo_inicio, destino, bonus = entrega
            idx_atual = destinos.index(local_atual)
            idx_destino = destinos.index(destino)

            # Calcula o tempo de deslocamento (somente ida)
            tempo_deslocamento = matriz_conexoes[idx_atual][idx_destino]

            # Calcula o novo tempo após o deslocamento
            novo_tempo = tempo_atual + tempo_deslocamento

            if novo_tempo <= tempo_inicio:
                novo_estado = {
                    "local_atual": destino,
                    "tempo_atual": novo_tempo,  # Atualiza o tempo após o deslocamento
                    "lucro": lucro_atual + bonus,  # Atualiza o lucro com o bônus da entrega
                    "entregas_restantes": [e for e in entregas_restantes if e != entrega],  # Remove a entrega já feita
                    "entregas_realizadas": entregas_realizadas + [(tempo_inicio, destino, bonus)]  # Atualiza a sequência de entregas realizadas
                }
                # Usar o contador para desambiguar casos com o mesmo custo estimado
                heapq.heappush(fronteira, (custo_estimado(novo_estado), len(novo_estado["entregas_restantes"]), next(contador), novo_estado))
            else:
                # Se não podemos entregar a tempo, apenas atualizamos o estado sem realizar essa entrega
                if lucro_atual > melhor_lucro:
                    melhor_lucro = lucro_atual
                    melhor_sequencia = entregas_realizadas

    return melhor_sequencia, melhor_lucro
