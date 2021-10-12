from random import sample

def inicializar():
    populacao = []
    for i in range(100):
        populacao.append(sample(range(1,9),8))
    return populacao

populacao = inicializar()
