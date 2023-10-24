def kthFactor(self, n: int, k: int) -> int:
        a=[]
        for i in range(1,n+1):
            if(n%i==0):
                a.append(i)
        if(len(a)<k):
            return -1
        else:
            return a[k-1]
