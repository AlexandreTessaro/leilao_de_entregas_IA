def calcular_lucro_basico(destinos, matriz_conexoes, entregas):
    local_atual = "A"
    tempo_atual = 0
    lucro_total = 0

    for entrega in entregas:
        tempo_inicio, destino, bonus = entrega
        idx_atual = destinos.index(local_atual)
        idx_destino = destinos.index(destino)

        # Tempo para ir e voltar
        tempo_deslocamento = matriz_conexoes[idx_atual][idx_destino] * 2
        
        if tempo_atual + tempo_deslocamento <= tempo_inicio:
            lucro_total += bonus
            tempo_atual += tempo_deslocamento
            local_atual = destino
    
    return lucro_total
