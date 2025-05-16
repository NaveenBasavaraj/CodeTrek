class PrimeNumberProblem:
    def countPrime(self, n):
        '''
        Sieve of Eratosthenes
        '''
        if n<2:
            return 0
        
        is_prime = [True for i in range(n)]
        is_prime[0] = isprime[1] = 1

        for i in range(2, math.ceil(math.sqrt(n))):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False
        return sum(is_prime)
