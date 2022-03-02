
'''
I'm assuming that all composite numbers have at least 1 divisor no greater than its square root


Let's prove this by contradiction

x is a composite number that doesn't have a divisor k less than or equal to its square root

x/k, k > root(x)

'''
def primes(n):
    primes = []
    is_prime = [False, False] + [True] * (n-1)

    # O(n log n) -> Sieving method
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i, n+1, i):
                is_prime[j] = False
    return primes

print(primes(18))