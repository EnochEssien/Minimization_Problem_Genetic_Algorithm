__author__ = "Enoch Essien"
__copyright__ = "Free Use"
__version__ = "3.1"
__maintainer__ = "Enoch Essien"
__email__ = "enochessien05@gmail.com"



# Relevant imports
import random
import math
import copy
import matplotlib.pyplot as plt


# Class for each solution
class individual:
    def ___init__(self, gene, fitness, N):
        self.gene = float[N]
        self.fitness = fitness


# First Minimisation function used as fitness test
def First_Minimisation_Function(individual, N):
    sum = 0

    for i in range(1, N - 1):
        x = individual.gene[i]
        y = 100 * (((x + 1 - (x ** 2)) ** 2) + ((1 - x) ** 2))
        sum = + y

    individual.fitness = sum


# Second Minimisation function used as fitness test swapped out of use from main code
def Second_Minimisation_Function(individual, N, M):
    sum = 0

    for i in range(1, N):
        x = individual.gene[i]
        y = math.sin(x) * (math.sin(i * (x ** 2) / (math.pi))) ** (2 * M)
        sum = + y
    individual.fitness = -1 * sum


# Function used to randomly fill genes of first population
def Initial_Population(N, P):
    Population = []

    for j in range(0, P):
        tempgene = []
        newind = individual()
        Pi = math.pi
        for i in range(0, N):
            """ Swaps out the out bound for the first minimisation function '-100 < x < 100' """
            tempgene.append(-100 + (100 - (-100)) * random.random())

            """ Swaps out the out bound for the Second minimisation function '0 < x < Pi' """
            #tempgene.append( 0 + (Pi-(0))*random.random())

        newind.gene = tempgene.copy()
        Population.append(newind)
    return Population


# Function used for selection, specifically tournament selection
def Tournament_Selection(Population, P):
    parents = []
    for i in range(0, P):
        off1 = random.randint(0, P - 1)

        off2 = random.randint(0, P - 1)

        if Population[off1].fitness < Population[off2].fitness:
            parents.append(copy.deepcopy(Population[off1]))
        else:
            parents.append(copy.deepcopy(Population[off1]))
    return parents


# Selection Function using the roulette wheel method
def Roulette_Wheel_Selection(population):
    parents = []
    total_fitness = calc_total_fitness(population)

    for i in range(0, len(population)):
        selection_point = random.uniform(0, total_fitness)
        running_total = 0
        j = 0
        while running_total >= selection_point:
            running_total += population[j].fitness
            j = j + 1
        parents.append(copy.deepcopy(population[j - 1]))
        # print(parents[i].gene, "Fitness:", parents[i].fitness)
    calc_total_fitness(parents)
    return parents


# Function used for single point crossover of two parents to produce an two offsprings
def Crossover(Offspring, P, N, CrossoverRate):
    for x in range(0, P, 2):
        CrossProb = random.randint(0, 100)
        if CrossProb < (100 * CrossoverRate):
            temp = Offspring[x]
            crosspoint = random.randint(0, N)
            for y in range(crosspoint, N):
                Offspring[x].gene[y] = Offspring[x + 1].gene[y]
                Offspring[x + 1].gene[y] = temp.gene[y]


# Function used for mutating the genes of an individual using real value mutation
def Mutation(Offspring, P, N, Muterate, MutateStep):
    for i in range(0, P):

        for j in range(0, N):
            alter = 0 + (MutateStep - 0) * random.random()
            gene = Offspring[i].gene[j]
            mutprob = random.randint(0, 100)
            operator = random.randint(0, 1)
            if mutprob < (100 * Muterate):
                if operator == 1:
                    Offspring[i].gene[j] = gene - alter
                else:
                    Offspring[i].gene[j] = gene + alter


# Function used to keep track of the best fitness seen in a given generation
def Best_Fitness(Population, P):
    Best_Fit = Population[0].fitness

    for x in range(0, P):
        if Best_Fit > Population[x].fitness:
            Best_Fit = Population[x].fitness

    return Best_Fit


# Function used to keep track of the best individual seen in a given generation
def Best_Genes(Population, P):
    Best_Gene = 0
    Best_Fit = Population[0].fitness

    for x in range(0, P):
        if Best_Fit > Population[x].fitness:
            Best_Fit = Population[x].fitness
            Best_Gene = x

    return Best_Gene


# Function used to keep track of the average fitness of a given generation
def Mean_Fitness(Population, P):
    Total = 0

    for x in range(0, P):
        Total += Population[x].fitness

    Mean_Fit = Total / P
    return Mean_Fit


# Function calculates hte total fitness of a population
def calc_total_fitness(population):
    MaxFit = 0
    for i in range(0, len(population)):
        MaxFit += population[i].fitness

    return MaxFit

# Function for generating a line graph of the best fitness seen and average fitness through all the generations
def create_graph(mean_score_progress, top_score_progress):
    graph_values = range(0, len(mean_score_progress))
    plt.xlabel("Number of Generations")
    plt.ylabel("Fitness Value")
    plt.plot(graph_values, mean_score_progress, label="Mean Fitness")
    plt.plot(graph_values, top_score_progress, label="Top Fitness")
    plt.legend()
    plt.show()

"""Main Body of Code"""

# Initial constants

P = 50  # Population size
N = 20  # Number og genes
M = 10  # Control parameter for second minimisation function to control optima steepness
G = 500  # Generation size

""" Results many change depending on which crossover/Mutation probability and mutation step is used, adjust depending on which minimisation function is in use"""
MutateRate = 0.05  # Rate of mutation, chances of a gene being mutated
MutateStep = 0.01  # adds or subtracts a random value in this range from specific gene to provide real value mutation
CrossoverRate = 0.1  # Rate of crossover, chanes of crossover happening between two values

# Initial population is produced
Population = Initial_Population(N, P)

# Fitness test of intial population
for y in range(0, P):
    """ Swaps out the two minimisation functions depending on which is in use, Make sure to comment out the proper bounds when initializing the population"""
    First_Minimisation_Function(Population[y], N)
    #Second_Minimisation_Function(Population[y],N,M)

# Tracks the average fitness, Best individual and Best fitness of first generation
Best_Fit = Best_Fitness(Population, P)
Best_Gene = Best_Genes(Population, P)
Mean_Fit = Mean_Fitness(Population, P)

# Prints Results
print('Initial Population')
print('Average Fitness of Generation = ', Mean_Fit)
print('Best Fitness of Generation = ', Best_Fit)
print('Best Genes of Generation = ', Best_Gene)

Best_Solution = Best_Fit  # Variable to track best fitness seen in all generations
Best_Solution_Genes = Population[Best_Gene].gene  # Variable to track best genes seen in all generations
Best_Generation = 0  # Variable to track of the generation with the best fitness seen in all generations
Best_Average_Fitness = Mean_Fit  # Variable to track of the generation with the best average fitness seen in all generations
Best_Gen_Average = 0  # Variable to track of the generation with the best average fitness

Average_Fitness_Progress = []
Best_Fitness_Progress = []

# Runs for amount of generations
for x in range(0, G):

    """Calls the selection function for the code, either tournament selection or roulette wheel functions, depending on which is commented our"""
    #Parents = Tournament_Selection(Population, P)
    Parents = Roulette_Wheel_Selection(Population)

    #creates deep copies of the parent population to be used in the offspring populaiton
    Offspring = []
    for i in range(0, P):
        Offspring.append(copy.deepcopy(Parents[i]))

    # calls crossover function on new population
    Crossover(Offspring, P, N, CrossoverRate)

    # calls Mutation function on new population
    Mutation(Offspring, P, N, MutateRate, MutateStep)

    # Replaces old population with the new one, using deep copies
    Population = []
    for k in range(0, P):
        Population.append(copy.deepcopy(Offspring[k]))

    # Fitness test of intial population
    for z in range(0, P):
        """ Swaps out the two minimisation functions depending on which is in use, Make sure to comment out the proper bounds when initializing the population"""
        First_Minimisation_Function(Population[z], N)
        #Second_Minimisation_Function(Population[z], N, M)

    # Tracks the average fitness, Best individual and Best fitness of first generation
    Best_Fit = Best_Fitness(Population, P)
    Best_Gene = Best_Genes(Population, P)
    Mean_Fit = Mean_Fitness(Population, P)

    # Supposed to keep track of the individual with the lowest fitness, genes and the generation that holds it
    if Best_Fit < Best_Solution:
        Best_Solution = Best_Fit
        Best_Generation = x
        Best_Solution_Genes = Population[Best_Gene].gene

    # Supposed to keep track of the generation with the lowest average fitness
    if Mean_Fit < Best_Average_Fitness:
        Best_Average_Fitness = Mean_Fit
        Best_Gen_Average = x

    #creates an array of the average fitness and best fitness seen in the generation to be used to plot graph
    Average_Fitness_Progress.append( Mean_Fit )
    Best_Fitness_Progress.append(Best_Fit)


    # Prints Results for the average fitness, best fitness and best individual of this generation
    print('Generation : ', x)
    print('Average Fitness of Generation = ', Mean_Fit)
    print('Best Fitness of Generation = ', Best_Fit)
    print('Best Individual of Generation = ', Best_Gene)

#prints out the best
print("                                              ")
print("Generation with the best average fitness", Best_Gen_Average, "With an average of ", Best_Average_Fitness)
print('Best Fitness seen in run = ', Best_Solution, ' Seen in Generation', Best_Generation)



#Generates a graph of results
create_graph(Average_Fitness_Progress, Best_Fitness_Progress)

