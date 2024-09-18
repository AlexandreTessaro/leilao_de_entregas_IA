from src.leitura_dados import ler_conexoes, ler_entregas
from src.leilao_basico import calcular_lucro_basico
from src.leilao_otimizado import calcular_lucro_otimizado
from src.comparar_desempenho import comparar_desempenho

def main():
    # Lê as conexões e as entregas
    destinos, conexoes = ler_conexoes()
    entregas = ler_entregas()

    # Executar a versão básica do leilão de entregas
    print("Executando Leilão de Entregas - Versão Básica")
    entregas_realizadas_basico, lucro_basico = calcular_lucro_basico(destinos, conexoes, entregas)
    
    # Exibir a sequência de entregas da versão básica
    print("Entregas realizadas (básico):")
    for entrega in entregas_realizadas_basico:
        tempo_inicio, destino, bonus = entrega
        print(f"({tempo_inicio}, {destino}; {bonus})")
    
    print(f"Lucro esperado (básico): {lucro_basico}")

    # Executar a versão otimizada do leilão de entregas
    print("\nExecutando Leilão de Entregas - Versão Otimizada")
    entregas_realizadas_otimizado, lucro_otimizado = calcular_lucro_otimizado(destinos, conexoes, entregas)
    
    # Exibir a sequência de entregas da versão otimizada
    print("Entregas realizadas (otimizado):")
    for entrega in entregas_realizadas_otimizado:
        tempo_inicio, destino, bonus = entrega
        print(f"({tempo_inicio}, {destino}; {bonus})")
    
    print(f"Lucro esperado (otimizado): {lucro_otimizado}")

    comparar_desempenho(destinos, conexoes, entregas)

if __name__ == "__main__":
    main()
