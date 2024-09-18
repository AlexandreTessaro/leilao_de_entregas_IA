def ler_conexoes():
    destinos = ["A", "B", "C", "D"]
    matriz_conexoes = [
        [0, 5, 0, 2],
        [5, 0, 3, 0],
        [0, 3, 0, 8],
        [2, 0, 8, 0]
    ]
    return destinos, matriz_conexoes

def ler_entregas():
    entregas = [
        (0, "B", 1),
        (5, "C", 10),
        (10, "D", 8)
    ]
    return entregas
