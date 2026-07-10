class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            elif stack:
                if i == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif i == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif i == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
            else:
                return False
        return not stack
        