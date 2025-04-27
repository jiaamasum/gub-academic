import random

def create_individual(k):
    
    return [random.randint(1, 9) for _ in range(k)]

def calculate_fitness(individual, target):
    total = sum(individual)

    if total != target:
        return -1000 - abs(total - target)  

    if 0 in individual:
        return -2000  

    avg_value = sum(individual) / len(individual)
    max_value = max(individual)
    spread = max(individual) - min(individual)
    
    
    fitness = -(max_value * 5 + spread * 2 + avg_value)
    return fitness

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.randint(1, 100) <= mutation_rate:
            individual[i] = random.randint(1, 9)  

def crossover(parent1, parent2):
    cut = random.randint(1, len(parent1) - 1)
    child = parent1[:cut] + parent2[cut:]
    return child

def selection(population, fitnesses):
    sorted_indices = sorted(range(len(population)), key=lambda i: fitnesses[i], reverse=True)
    return population[sorted_indices[0]], population[sorted_indices[1]]

if __name__ == "__main__":
    target = int(input("T = "))
    k = int(input("k = "))
    mutation_rate = 30  
    pop_size = 20       
    max_generations = 1000

    population = [create_individual(k) for _ in range(pop_size)]

    for generation in range(max_generations):
        fitnesses = [calculate_fitness(ind, target) for ind in population]
        best_idx = fitnesses.index(max(fitnesses))
        best_individual = population[best_idx]

        if sum(best_individual) == target and 0 not in best_individual:
            break

        new_generation = []
        for _ in range(pop_size):
            parent1, parent2 = selection(population, fitnesses)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_generation.append(child)

        population = new_generation

    
    print(*sorted(population[best_idx]))
