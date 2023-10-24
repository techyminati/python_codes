def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=max(piles)
        while(l<=r):
            s=0
            k=(l+r)//2
            for p in piles:
                s+=math.ceil(p/k)
            if(s<=h):
                res=min(res,k)
                r=k-1
            else:
                l=k+1
        return res
