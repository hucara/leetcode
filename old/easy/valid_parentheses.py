class Solution:
    def isValid(self, s: str) -> bool:
        transitions = {"]": "[", "}": "{", ")": "("}

        stack = []
        for c in s:
            if c in list(transitions.keys()):
                if stack and stack[-1] == transitions[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if stack:
            return False
        else:
            return True
