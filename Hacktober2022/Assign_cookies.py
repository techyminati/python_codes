class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        c = 0
        while len(g) != 0 and len(s) != 0 :
            if g[0] <= s[0] :
                c = c + 1
                del g[0]
                del s[0]
            else :
                del s[0]
        return c
