from collections import Counter

def combine_factors(factors1, factors2):
    count1 = Counter(factors1)
    count2 = Counter(factors2)
    combined_factors = []
    all_primes = set(count1.keys()).union(set(count2.keys()))
    for prime in all_primes:
        max_count = max(count1.get(prime, 0), count2.get(prime, 0))
        combined_factors.extend([prime] * max_count)
    return combined_factors