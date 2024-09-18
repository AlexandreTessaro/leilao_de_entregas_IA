import heapq

def calcular_lucro_otimizado(destinos, matriz_conexoes, entregas):
    # Função para estimar o custo do estado atual
    def custo_estimado(estado):
        return -estado["lucro"]  # Usar negativo para maximizar o lucro (heapq é uma min-heap)

    # Estado inicial
    estado_inicial = {
        "local_atual": "A",  # Sempre começando no ponto A
        "tempo_atual": 0,
        "lucro": 0,
        "entregas_restantes": entregas
    }
    
    fronteira = []
    heapq.heappush(fronteira, (custo_estimado(estado_inicial), estado_inicial))
    melhor_lucro = 0

    while fronteira:
        _, estado_atual = heapq.heappop(fronteira)

        local_atual = estado_atual["local_atual"]
        tempo_atual = estado_atual["tempo_atual"]
        lucro_atual = estado_atual["lucro"]
        entregas_restantes = estado_atual["entregas_restantes"]
        
        # Se não há mais entregas restantes, atualiza o melhor lucro
        if not entregas_restantes:
            melhor_lucro = max(melhor_lucro, lucro_atual)
            continue
        
        # Testa cada entrega possível
        for entrega in entregas_restantes:
            
            tempo_inicio, destino, bonus = entrega
            idx_atual = destinos.index(local_atual)
            idx_destino = destinos.index(destino)

            # Calcula o tempo de deslocamento (somente ida)
            tempo_deslocamento = matriz_conexoes[idx_atual][idx_destino]

            # Agora, vamos permitir que a entrega seja feita mesmo que o tempo de deslocamento seja maior que o tempo de início da próxima entrega
            novo_tempo = tempo_atual + tempo_deslocamento

            if novo_tempo <= tempo_inicio:
                novo_estado = {
                    "local_atual": destino,
                    "tempo_atual": novo_tempo,  # Atualiza o tempo após o deslocamento
                    "lucro": lucro_atual + bonus,  # Atualiza o lucro com o bônus da entrega
                    "entregas_restantes": [e for e in entregas_restantes if e != entrega]  # Remove a entrega já feita
                }
                heapq.heappush(fronteira, (custo_estimado(novo_estado), novo_estado))
            else:
                # Se não podemos entregar a tempo, apenas atualizamos o estado sem realizar essa entrega
                melhor_lucro = max(melhor_lucro, lucro_atual)

    return melhor_lucro
