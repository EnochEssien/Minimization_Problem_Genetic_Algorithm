# Summary
The aim of this project was to create a program that can provide the closest solution to the two minimization function seen below. 

![image](https://user-images.githubusercontent.com/91120304/161843576-2b6a7dab-95dc-45fb-8063-07b5bfcf9970.png)

As such for this challenge a genetic algorithm was implemented. 
The two functions can be commented out of the code depending on which solution is being found. 
As well as two "selection methods" were used to compare the effectiveness, each can be swapped out as well. 



**Installation**

There isn't much installation needed, as long as one has a suitable Python editor.

**Dependecies and Libraries**

1. Python 3 and above
2. random: Provides functions for generating random numbers.
3. math: Provides mathematical functions and constants.
4. copy: Provides functions for creating copies of objects.
5. matplotlib.pyplot: Provides functions for creating graphs and plots.

**How It Works** 

This script is quite flexible, used as a training tool to analyze how changing various functions and variables affects the end results and output.

***Variables***

*Population Size* : number of candidates per generation

*Number of Genes* : number of genes in a candidate

*Mutation Rate* : chance of a candidates genes changing 

*Mutation Step* : how much a gene changes by

*Generation Size* : number of iterations of the algorithm

*Crossover Rate* : chance of which two candidates genes would be swapped to make a new generation, Only used in the "Tournament Selection" Function

 

***Functions***

*First_Minimisation_Function(individual, N)*
This function calculates the fitness value of an individual for the first minimization function. The fitness value is computed based on the individual's genes. The parameter N represents the number of genes in the individual.

*Second_Minimisation_Function(individual, N, M)*
This function calculates the fitness value of an individual for the second minimization function. The fitness value is computed based on the individual's genes. The parameters N and M represent the number of genes and a control parameter for the second function, respectively. This function is currently commented out and not used in the main code.

*Initial_Population(N, P)*
This function generates the initial population of individuals. It randomly fills the genes of each individual based on the given number of genes (N) and the population size (P).

*Tournament_Selection(Population, P)*
This function performs tournament selection to select parents for the next generation. It randomly selects two individuals from the population and chooses the one with the lower fitness value as the parent. This process is repeated for each parent needed for the next generation.

*Roulette_Wheel_Selection(population)*
This function performs roulette wheel selection to select parents for the next generation. The selection probability of an individual is proportional to its fitness value. It randomly selects individuals until the required number of parents is selected.

*Crossover(Offspring, P, N, CrossoverRate)*
This function performs single-point crossover between pairs of parents to generate offspring for the next generation. The crossover rate (CrossoverRate) determines the probability of crossover occurring between two individuals.

*Mutation(Offspring, P, N, Muterate, MutateStep)*
This function performs mutation on the offspring population. It randomly mutates the genes of individuals with a probability determined by the mutation rate (Muterate). The mutation step (MutateStep) controls the range of mutation.

*Best_Fitness(Population, P)*
This function calculates the best fitness value among the individuals in a given population.

*Best_Genes(Population, P)*
This function returns the index of the individual with the best fitness value in a given population.

*Mean_Fitness(Population, P)*
This function calculates the average fitness value of the individuals in a given population.

*calc_total_fitness(population)*
This function calculates the total fitness of a population by summing up the fitness values of all individuals.

*create_graph(mean_score_progress, top_score_progress)*
This function generates a line graph of the best fitness value and average fitness value observed throughout the generations. It uses the matplotlib library to create the graph.


**Example Output**

This is an example of what kind of output when one runs the algorithm, ![image](https://github.com/EnochEssien/Minimization_Problem_Genetic_Algorithm/assets/91120304/0fa70a3c-bed3-479d-9e3e-8fb8f9505264)


And here is a graph depicting how the algorithm produces a smaller and smaller solution which matches the purpose of a "Minimization function" 

![Minimization](https://github.com/EnochEssien/Minimization_Problem_Genetic_Algorithm/assets/91120304/bfc71807-6eed-49ec-bb2e-51ce98a0c571)

