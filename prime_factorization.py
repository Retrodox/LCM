def prime_factors(unfactored_numbers):
    i = 2
    factored_numbers = []
    while i * i <= unfactored_numbers:
        if unfactored_numbers % i:
            i += 1
        else:
            unfactored_numbers //= i
            factored_numbers.append(i)
    if unfactored_numbers> 1:
        factored_numbers.append(unfactored_numbers)
    return factored_numbers