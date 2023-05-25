class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        popen = "([{"
        pclosed = ")]}"
        for char in s:
            if char in popen:
                stack.append(char)
            else:
                if stack == []:
                    return False
                if not pclosed.index(char) == popen.index(stack[-1]):
                    return False
                stack.pop()
        return stack == []