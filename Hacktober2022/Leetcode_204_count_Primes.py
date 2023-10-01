class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True]*n #to make all list element values true
        if n<2:
            return 0
        else:
            prime[1] = prime[0] = False
            for i in range(2,n):
                if prime[i] is not False:
                    prime[i] = True
                for j in range(i*i,n,i):
                    prime[j] = False
        return sum(prime)#it will return sum of all True(1) values only