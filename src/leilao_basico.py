def calcular_lucro_basico(destinos, matriz_conexoes, entregas):
    local_atual = "A"
    tempo_atual = 0
    lucro_total = 0
    entregas_realizadas = []

    for entrega in entregas:
        tempo_inicio, destino, bonus = entrega
        idx_atual = destinos.index(local_atual)
        idx_destino = destinos.index(destino)

        # Tempo para ir e voltar
        tempo_deslocamento = matriz_conexoes[idx_atual][idx_destino] * 2
        
        if tempo_atual + tempo_deslocamento <= tempo_inicio:
            lucro_total += bonus
            tempo_atual += tempo_deslocamento
            entregas_realizadas.append((tempo_inicio, destino, bonus))
            local_atual = destino
    
    return entregas_realizadas, lucro_total

def processar_entregas(conexoes, entregas):
    entregas_realizadas = []
    tempo_atual = 0  
    lucro_total = 0  

    local_atual = 'A'

    for entrega in entregas:
        tempo_saida, destino, bonus = entrega

        tempo_ate_destino = conexoes[local_atual][destino]
        tempo_retorno = conexoes[destino]['A']

        if tempo_atual + tempo_ate_destino <= tempo_saida:
            tempo_atual += tempo_ate_destino + tempo_retorno

            lucro_total += bonus

    return entregas_realizadas, lucro_total