from collections import Counter

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def combine_factors(factors1, factors2):
    count1 = Counter(factors1)
    count2 = Counter(factors2)
    combined_factors = []
    all_primes = set(count1.keys()).union(set(count2.keys()))
    for prime in all_primes:
        max_count = max(count1.get(prime, 0), count2.get(prime, 0))
        combined_factors.extend([prime] * max_count)
    return combined_factors

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    factors1 = prime_factors(num1)
    factors2 = prime_factors(num2)
    
    final_factors = combine_factors(factors1, factors2)
    
    result = 1
    for factor in final_factors:
        result *= factor
    
    print("The result of combining the prime factorizations is:", result)

if __name__ == "__main__":
    main()
