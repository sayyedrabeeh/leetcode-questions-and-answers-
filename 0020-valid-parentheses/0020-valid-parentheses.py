class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for i in s:
            if i not in mapping:
                stack.append(i)
            else:
                if not stack or stack.pop() != mapping[i]:
                    return False
        return not stack