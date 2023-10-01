class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        stack=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                elif i==')':
                    if stack[-1]=='(':
                        stack.pop()
                    else:
                        return False
                elif i==']':
                    if stack[-1]=='[':
                        stack.pop()
                    else:
                        return False
                elif i=='}':
                    if stack[-1]=='{':
                        stack.pop()
                    else:
                        return False
        if len(stack)==0:
            return True
        else:
            return False
