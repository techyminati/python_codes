def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for id in asteroids:
            if not stack or stack[-1]*id>0 or stack[-1]<0:
                stack.append(id)
            elif abs(id)>=abs(stack[-1]):
                while stack and stack[-1]>0 and abs(id) > abs(stack[-1]):
                    stack.pop()
                if not stack or stack[-1]<0:
                    stack.append(id)
                elif stack[-1] == -id:
                    stack.pop()
        return stack
