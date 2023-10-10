//Restore IP Address leetcode problem
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def backtrack(path, s):
            if len(path) == 4 and len(s) == 0: 
                ans.append(".".join(path))
            for i in range(1, len(s) + 1):
                num = s[:i]
                if int(num) > 255 or (num[0] == "0" and len(num) > 1):continue
                path.append(num)
                backtrack(path, s[i:])
                path.pop()
        backtrack([], s)
        return ans
