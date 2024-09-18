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
    # Lista para armazenar as entregas realizadas
    entregas_realizadas = []
    tempo_atual = 0  # O tempo inicial é 0
    lucro_total = 0  # Acumulador do lucro

    # Inicialmente, estamos no ponto A
    local_atual = 'A'

    # Processar as entregas uma a uma
    for entrega in entregas:
        # Obter dados da entrega
        tempo_saida, destino, bonus = entrega

        # Verificar o tempo necessário para ir ao destino e voltar
        tempo_ate_destino = conexoes[local_atual][destino]
        tempo_retorno = conexoes[destino]['A']

        # Se houver tempo disponível para realizar a entrega
        if tempo_atual + tempo_ate_destino <= tempo_saida:
            # Atualiza o tempo atual
            tempo_atual += tempo_ate_destino + tempo_retorno
            # Realizar a entrega
            entregas_realizadas.append((tempo_saida, destino, bonus))
            # Atualiza o lucro total
            lucro_total += bonus

    return entregas_realizadas, lucro_total