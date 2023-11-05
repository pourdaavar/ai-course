import random
import math


def generate_genome(genome_length):
    """
    Generates a random genome of a given length.

    Parameters:
        genome_length (int): The length of the genome to be generated.

    Returns:
        list: A list representing the generated genome, where each element is either 0 or 1.
    """
    return [random.randint(0, 1) for _ in range(genome_length)]


def generate_chromosome(x_len, y_len):
    """
    Generates a chromosome of a given length.

    Parameters:
        chromosome_length (int): The length of the chromosome to be generated. Defaults to 10.

    Returns:
        list: A list representing the generated chromosome, where each element is either 0 or 1.
    """
    return generate_genome(x_len) + generate_genome(y_len)


def decode_chromosome(chromosome, x_len, y_len):
    chromosome_length = len(chromosome)

    binary_x = "".join(map(str, chromosome[:x_len]))
    binary_y = "".join(map(str, chromosome[y_len:]))

    x = int(binary_x, 2)
    y = int(binary_y, 2)

    return x / (2 ** x_len), y / (2 ** y_len)


def objective_function(x, y):
    return math.sin(x + y**2)


def do_crossover(parent1, parent2, crossover_rate=0.8):
    child1, child2 = parent1, parent2
    if random.random() < crossover_rate:
        crossover_point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


def do_mutation(chromosome, mutation_rate=0.01):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]
    return chromosome


# Define the chromosome length and population size
x_binary_length = 9
y_binary_length = 5
chromosome_length = x_binary_length + y_binary_length  # Binary representation

population_size = 11
generations = 10
mutation_rate = 0.1


# Function to calculate the fitness of a chromosome
def calculate_fitness(chromosome):
    x, y = decode_chromosome(
        chromosome, x_len=x_binary_length, y_len=y_binary_length)
    return objective_function(x, y)


def tournament_selection(population, tournament_size):
    selected_parents = []
    for _ in range(len(population)):
        tournament = random.sample(population, tournament_size)

        best_chromosome = max(tournament, key=calculate_fitness)
        selected_parents.append(best_chromosome)
    return selected_parents


# Initialize the population
population = [generate_chromosome(x_binary_length, y_binary_length)
              for _ in range(population_size)]


# Main genetic algorithm loop
for generation in range(generations):
    # Select parents using tournament selection
    selected_parents = tournament_selection(population, tournament_size=2)

    # Create a new generation through crossover and mutation
    new_population = []
    while len(new_population) < population_size:
        parent1, parent2 = random.sample(selected_parents, 2)
        child1, child2 = do_crossover(parent1, parent2)
        child1 = do_mutation(child1, mutation_rate)
        child2 = do_mutation(child2, mutation_rate)
        new_population.extend([child1, child2])

    population = new_population

# Find the best solution in the final population
best_chromosome = max(population, key=calculate_fitness)
best_x, best_y = decode_chromosome(
    best_chromosome, x_len=x_binary_length, y_len=y_binary_length)
best_fitness = calculate_fitness(best_chromosome)

print(f"Best solution: x = {best_x}, y = {best_y}, Fitness = {best_fitness}")
