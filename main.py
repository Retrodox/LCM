from combine_factors import combine_factors
from prime_factorization import prime_factors

def calculate_lcm():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    factors1 = prime_factors(num1)
    factors2 = prime_factors(num2)

    final_factors = combine_factors(factors1, factors2)
    print(final_factors)
    result = 1
    for factor in final_factors:
        result *= factor

    print(f"The Least Common Multiple for {num1} and {num2} is: {result}")


while True:
     calculate_lcm()
     answer = input("Would you like to keep going? (Y/N): ").strip().lower()
     if answer in ["no", "n"]:
        break
