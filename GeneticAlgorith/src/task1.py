import random
import numpy as np

# 1. 评估个体的目标函数值
def evaluate(individual):
    x1, x2 = individual
    f1 = (x1 ** 2) / 4  # 目标函数 f1
    f2 = x1 * (1 - x2) + 5  # 目标函数 f2
    return f1, f2

# 2. 初始化种群
def init_population(pop_size):
    population = []
    for _ in range(pop_size):
        x1 = random.uniform(1, 4)
        x2 = random.uniform(1, 2)
        individual = [x1, x2]
        population.append(individual)
    return population

# 3. 帕累托支配判定
def dominates(ind1, ind2):
    f1_1, f1_2 = evaluate(ind1)
    f2_1, f2_2 = evaluate(ind2)
    return (f1_1 <= f2_1 and f1_2 <= f2_2) and (f1_1 < f2_1 or f1_2 < f2_2)

# 4. 帕累托排序
def pareto_sort(population):
    pareto_front = []
    for i, ind1 in enumerate(population):
        dominated = False
        for j, ind2 in enumerate(population):
            if dominates(ind2, ind1):
                dominated = True
                break
        if not dominated:
            pareto_front.append(ind1)
    return pareto_front

# 5. 选择操作（轮盘赌选择基于帕累托排序的个体）
def select(population, num_to_select):
    selected = []
    pareto_front = pareto_sort(population)
    while len(selected) < num_to_select:
        selected.append(random.choice(pareto_front))
    return selected

# 6. 交叉操作
def crossover(parent1, parent2):
    alpha = random.random()
    child1 = [alpha * p1 + (1 - alpha) * p2 for p1, p2 in zip(parent1, parent2)]
    child2 = [(1 - alpha) * p1 + alpha * p2 for p1, p2 in zip(parent1, parent2)]
    return child1, child2

# 7. 变异操作
def mutate(individual, mutation_rate=0.1):
    if random.random() < mutation_rate:
        idx = random.randint(0, 1)
        if idx == 0:
            individual[0] = random.uniform(1, 4)
        else:
            individual[1] = random.uniform(1, 2)

# 8. 主算法流程
def main():
    pop_size = 100  # 种群大小
    generations = 200  # 代数
    crossover_rate = 0.7  # 交叉概率
    mutation_rate = 0.1  # 变异概率

    # 初始化种群
    population = init_population(pop_size)

    for gen in range(generations):
        new_population = []

        # 选择操作
        selected = select(population, pop_size)

        # 交叉操作
        for i in range(0, pop_size, 2):
            if random.random() < crossover_rate:
                parent1, parent2 = selected[i], selected[i+1]
                child1, child2 = crossover(parent1, parent2)
                new_population.extend([child1, child2])
            else:
                new_population.extend([selected[i], selected[i+1]])

        # 变异操作
        for individual in new_population:
            mutate(individual, mutation_rate)

        # 更新种群
        population = new_population

        # 输出帕累托前沿解
        pareto_front = pareto_sort(population)
        print(f"Generation {gen}: Pareto front size = {len(pareto_front)}")

    # 输出最终帕累托前沿解
    pareto_front = pareto_sort(population)
    print("\nFinal Pareto front solutions:")
    for ind in pareto_front:
        print(f"Solution: {ind}, Objectives: {evaluate(ind)}")

if __name__ == "__main__":
    main()
