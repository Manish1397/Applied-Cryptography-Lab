def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_primes(limit):
    primes = []
    for i in range(2, limit + 1):
        if is_prime(i):
            primes.append(i)
    return primes


limit = int(input("Enter the limit: "))
print("Primes up to", limit, ":", generate_primes(limit))
