from random import randint, sample, random, seed 
 
def inicializar(): 
    populacao = [] 
    for i in range(100): 
        populacao.append(sample(range(1,9),8)) 
    return populacao 
 
def selecionar_pais(populacao): 
    indexs = sample(range(0,99),5) 
    pais = []
    for x in indexs: 
        a,b,a_aval,b_aval = 0,0,0,0
        x_aval = avaliar_configuracao(populacao[x])
        if(x_aval > a_aval):
            a_aval =x_aval
            a = x
        if(x_aval > b_aval and x_aval < a_aval):
            b_aval = x_aval
            b = x   
        pais = [populacao[a], populacao[b]] 
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

def recombinacao(pais):
    recombine = randint(1,10)
    if( recombine <=9):
        cut = randint(0,7)
        filho_a = pais[0][0:cut]
        filho_b = pais[1][0:cut]
        return [crossfill(filho_a,pais[1], cut+1), crossfill(filho_b,pais[0], cut+1)]
    else:
        return [pais[0],pais[1]]

def crossfill(filho, pai, index):
    if(index >=8):
        index = 0

    if (len(filho) == 8):
        return filho
    pai_index = index -1
    if(pai[pai_index] not in filho):
        filho.append(pai[pai_index])
        crossfill(filho,pai,index+1)
    else:
        crossfill(filho,pai,index+1)

    return filho

def mutacao(individuo):
    mutate = randint(1,10)
    if(mutate<=4):
        print('houve mutacao')
        index_a, index_b = randint(0,7),randint(0,7)
        print('Individuo antes ', individuo)
        individuo[index_a], individuo[index_b]= individuo[index_b],individuo[index_a]
        print("Individuo depois", individuo)
    return individuo

def avaliar_selecionar(populacao,filhos):
    avaliacoes_fitness = []
    for individuo in populacao:
        avaliacoes_fitness.append((individuo, avaliar_configuracao(individuo)))
    avaliacoes_fitness.sort(key= lambda x :x[1])
     
    print(avaliacoes_fitness)
    return populacao
             
# seed(1) 
populacao = inicializar() 
pais = selecionar_pais(populacao) 
print(pais)
filhos = recombinacao(pais)
for filho in filhos:
    filho = mutacao(filho)
print(filhos)
avaliar_selecionar(populacao,filhos)