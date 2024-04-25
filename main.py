from find_lcm import combine_factors
from prime_factorization import prime_factors


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
    
factors1 = prime_factors(num1)
factors2 = prime_factors(num2)

final_factors = combine_factors(factors1, factors2)
print(final_factors)
result = 1
for factor in final_factors:
    result *= factor

print("The result of combining the prime factorizations is:", result)
