from random import randint, sample, random, seed 
 
def inicializar(): 
    populacao = [] 
    for i in range(100): 
        populacao.append(sample(range(1,9),8)) 
    return populacao 
 
def selecionar_pais(populacao): 
    indexs = sample(range(1,101),5) 
    for x in indexs: 
 
     
    # pais = [populacao[indexs[0]], populacao[[indexs[1]]]] 
       return pais 
 
 
def avaliar_configuracao(candidato): 
    penalidade_rainhas = 0 
    for coluna in range(0,8): 
        penalidade_rainha = 0 
        rainha = candidato[coluna] 
        for r_checa in range(0,8): 
            if (r_checa == coluna): 
                continue 
            diferenca = abs(coluna - r_checa) 
            if candidato[r_checa == rainha + diferenca] or candidato[r_checa == rainha - diferenca]: 
                penalidade_rainha += 1 
        penalidade_rainhas += penalidade_rainha 
    return 1/(1+penalidade_rainhas)
             
seed(1) 
populacao = inicializar() 
# pais = selecionar_pais(populacao) 
print(populacao[0]) 
print(avaliar_configuracao(populacao[0]))