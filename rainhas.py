from random import randint, sample, random, seed

def inicializar():
    populacao = []
    for i in range(100):
        populacao.append(sample(range(1,9),8))
    return populacao

def selecionar_pais(populacao):
    indexs = sample(range(1,101),5)
    candidatos = [populacao[indexs[0]], populacao[indexs[1]]]

    # pais = [populacao[indexs[0]], populacao[[indexs[1]]]]
    return pais

def avaliar_candidato(candidato):
    for coluna in range(0,8):
        penalidade_rainha = 0
        rainha = candidato[coluna]
        for checagem_direita in range(1, 8):
            indice_checagem = checagem_direita + coluna
            if(indice_checagem > 7):
                break
            else:
                prox_rainha = candidato[indice_checagem]
                print(prox_rainha == rainha + (indice_checagem - coluna))
                print(prox_rainha == rainha - (indice_checagem - coluna))
                print(f"rainha: {rainha} comp: {prox_rainha} indice: {checagem_direita}")


seed(1)
populacao = inicializar()
# pais = selecionar_pais(populacao)
print(populacao[0])
avaliar_candidato(populacao[0])