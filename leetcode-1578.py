class Solution:
    def minCost(self, colors: str, cost: List[int]) -> int:
        
        res = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                res += min(cost[i], cost[i-1])
                cost[i] = max(cost[i], cost[i-1])
        
        return res
