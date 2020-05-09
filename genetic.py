# run with python 2

import random
import matplotlib.pyplot as plt
utility_holder = []
max_utility = 2.0
population_size = 20
def prod(lst):
    x = 1
    for i in lst:
        x *= i
    return x

def abs(a):
    return a if a >= 0 else -a

def other_pile(pile):
    return [x for x in range(1, 11) if x not in pile]

def random_chromosome(): #making random chromosomes
    pile_len = random.randint(1, 10)
    pile = []
    while len(pile) != pile_len:
        x = random.randint(1,10)
        if x not in pile:
            pile.append(x)
    return pile

def utility(chromosome):
    return max_utility - ((abs(sum(chromosome) - 36) / 36.0) + (abs(prod(other_pile(chromosome)) - 360) / 360.0))
        
def reproduce(x, y): #doing cross_over between two chromosomes
    child_len = random.randint(1,10)
    p = list(set(x + y))
    child = []
    while len(p) > 0 and len(child) < child_len:
        c = random.choice(p)
        child.append(c)
        p.remove(c)
    while len(child) < child_len:
        child.append(random.choice(other_pile(child)))
    return child

def mutate(x):  #randomly changing the value of a random index of a chromosome
    if(len(x) > 0):
        return x[:-1]
    return x

def genetic_queen(population, utility):
    mutation_probability = 0.4
    new_population = []
    for i in range(len(population)):
        for j in range(i, len(population)):
            child = reproduce(population[i], population[j]) #creating two new chromosomes from the best 2 chromosomes
            if random.random() < mutation_probability:
                child = mutate(child)
            # print_chromosome(child)
            new_population.append(child)
            if utility(child) == max_utility:
                break
    new_population.sort(lambda a,b: 1 if utility(b) - utility(a) > 0 else -1)
    return new_population[:population_size]

def print_chromosome(chrom):
    print("Chromosome = {},  Utility = {}"
        .format(str(chrom), utility(chrom)))

population = [random_chromosome() for _ in range(population_size)]

generation = 1
while not max_utility in [utility(chrom) for chrom in population]:
    utility_holder += [(generation,utility(chrom)) for chrom in population]
    population = genetic_queen(population, utility)
    generation += 1

for chrom in population:
    if utility(chrom) == max_utility:
        print("One of the solutions: ")
        print_chromosome(chrom)
        break

_, plot = plt.subplots()
plot.set_xlabel('x')
plot.set_ylabel('f(x)')
for u in utility_holder:
    if u[1] != max_utility:
        plot.scatter(u[0], max(u[1], 0), s=50, c='green', marker='s')
    else:
        plot.scatter(u[0], u[1], s=50, c='red', marker='s')
plt.show()

           
            
    
