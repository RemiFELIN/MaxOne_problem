#!/usr/bin/env python3

import random

MAXGEN  = 100 #Nombre maximum de génération
POPSIZE = 100 #La taille de la population
N = 20 #La longueur d'un génome
PMUT = 0.01 #Probabilité d'une mutation
PX = 0.6 #Probabilité d'une recombination

random.seed()
pop = []

for i in range(POPSIZE):
    # On génère une liste d'individu de taille POPSIZE, les individus sont composés de 0 et de 1 (et sont de taille N)
    individu = []
    while len(individu) < N:
        individu.append(random.randint(0, 1))
    pop.append(individu)

def fitness(ind):
    count = 0
    for gen in pop[pop.index(ind)]:
        if gen == 1:
            count += 1
    return count

def selection(population):

    # Définition des variables
    newPop = []
    cumsumFitness = 0
    cumsumByIndex = []
    randomSequence = []

    # On calcule notre cumsum
    for ind in population:
        # On incrémente avec le fitness de chaques individus
        cumsumFitness += fitness(ind)
        # On défini un tableau bi dimentionnel
        result = [None] * 2
        result[0] = population.index(ind)
        result[1] = cumsumFitness
        cumsumByIndex.append(result)

    # On affiche le cumsum fitness
    print("Cumsum= ", cumsumFitness)

    # On affiche un message dans l'hypothèse où la solution arrive à son optimum
    if cumsumFitness == POPSIZE * N:
        print("\n-> OPTIMUM TROUVE !!!\n")

    # On détermine notre séquence aléatoire en fonction de notre cumsum final
    for i in range(POPSIZE):
        randomSequence.append(int(random.uniform(0, cumsumFitness)))

    # Enfin on sélectionne les individus à partir de la méthode décrite dans l'exemple du cours
    for j in randomSequence:
        for k in range(POPSIZE):
            if cumsumByIndex[k][1] >= j:
                newPop.append(population[cumsumByIndex[k][0]])
                break

    # On retourne la nouvelle population
    return newPop



def mutation(ind):
    randByPMUT = random.uniform(0, PMUT)
    for i in ind:
        if randByPMUT <= PMUT:
            if ind[i] == 1:
                ind[i] = 0
            else:
                ind[i] = 1



def crossover(first, second):
    #Point à partir duquel les séquences seront coupés
    cutPoint: int = int(random.uniform(0, N))
    #Replace
    index1 = pop.index(first)
    index2 = pop.index(second)
    pop[index1] = first[0:cutPoint] + second[cutPoint:]
    pop[index2] = second[0:cutPoint] + first[cutPoint:]



for g in range(MAXGEN):
    print("--------------\nETAPE ", g+1, ": ")
    pop = selection(pop)
    for ind in pop:
        mutation(ind)
    for i in range(0, POPSIZE, 2):
        if random.random() < PX:
            crossover(pop[i], pop[i+1])