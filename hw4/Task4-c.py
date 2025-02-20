import numpy as np

# Problem 1
n = 100000
bits = np.random.randint(0, 2, n)
avg_bits = np.mean(bits)
print(f"Problem 1 - Average of random bits: {avg_bits}") 

# Problem 2
p = 0.7
bits_prob = np.random.choice([0, 1], size=n, p=[1-p, p])
avg_bits_prob = np.mean(bits_prob)
print(f"Problem 2 - Average with probability {p} for 1: {avg_bits_prob}") 

# Problem 3
numbers = np.random.choice([-1, 1], size=n)
avg_numbers = np.mean(numbers)
print(f"Problem 3 - Average of -1 and 1: {avg_numbers}") 

# Problem 4
values = np.arange(1, 11)
probabilities = np.full(10, 1/10)
random_numbers = np.random.choice(values, size=n, p=probabilities)
avg_random_numbers = np.mean(random_numbers)
print(f"Problem 4 - Average of uniform numbers from 1 to 10: {avg_random_numbers}") 

# Problem 5a
uniform_numbers = np.random.uniform(0, 1, n)
avg_uniform = np.mean(uniform_numbers)
print(f"Problem 5a - Average of uniform(0,1): {avg_uniform}")  

# Problem 5b
exp_numbers = -np.log(np.random.uniform(0, 1, n))
avg_exp = np.mean(exp_numbers)
print(f"Problem 5b - Average of exponential distribution: {avg_exp}") 

# Problem 5c
normal_numbers = np.random.normal(5, 1, n)
avg_normal = np.mean(normal_numbers)
print(f"Problem 5c - Average of normal(5,1): {avg_normal}") 
