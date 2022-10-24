class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        
        if len(strs) == 1:
            return strs[0]
                    
        if strs[0] == "" or len(strs) == 0:
            return ""
                    
        for i in range(len(strs[0])):
            allOk = False
            temp = strs[0][i]
            
            for j in range(1, len(strs)):
                if len(strs[j]) >= (i + 1):
                    if strs[j][i] == temp:
                        allOk = True
                    else:
                        allOk = False
                        break
                else:
                    return result
                    
            if allOk == True:
                result += temp
            elif allOk == False:
                return result
            
        return result

# https://leetcode.com/problems/longest-common-prefix/discuss/2236438/Easy-Python-Solution-(45ms)