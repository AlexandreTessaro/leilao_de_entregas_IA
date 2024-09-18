from src.leitura_dados import ler_conexoes, ler_entregas
from src.leilao_basico import calcular_lucro_basico
from src.leilao_otimizado import calcular_lucro_otimizado
from src.comparar_desempenho import comparar_desempenho

def main():
    destinos, conexoes = ler_conexoes()
    entregas = ler_entregas()

    print("Executando Leilão de Entregas - Versão Básica")
    lucro_basico = calcular_lucro_basico(destinos, conexoes, entregas)
    print(f"Lucro esperado (básico): {lucro_basico}")

    print("\nExecutando Leilão de Entregas - Versão Otimizada")
    lucro_otimizado = calcular_lucro_otimizado(destinos, conexoes, entregas)
    print(f"Lucro esperado (otimizado): {lucro_otimizado}")

    # Comparar o desempenho das duas versões
    comparar_desempenho(destinos, conexoes, entregas)

if __name__ == "__main__":
    main()
