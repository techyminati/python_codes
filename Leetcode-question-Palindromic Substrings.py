class Solution:
    def countSubstrings(self, s: str) -> int: 
        n=len(s)
        c=0
        for i in range(n):
            for j in range(i+1,n+1):
                st=""
                if s[i:j]==st.join(reversed(s[i:j])):
                    c+=1
        return c
        
