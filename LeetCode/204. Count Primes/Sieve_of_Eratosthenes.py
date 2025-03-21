# Using Sieve of Eratosthenes for optimizing reasons...

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2 :
            return 0
        
        Prime = [True for i in range(n)]
        Prime[0] = Prime[1] = False

        for i in range(2, math.ceil(math.sqrt(n))):
            if Prime[i]:
                for j in range(i*i, n, i):
                    Prime[j] = False
        
        return sum(Prime)
