class Solution:
    def isValid(self, s: str) -> bool:
        stack, left, right = [], ("(", "{", "["), (")", "}", "]")
        for char in s:
            if char in left:
                stack.append(char)
            elif not stack or left.index(stack.pop()) != right.index(char):
                return False
        return not stack

obj = Solution()
s = "()[]{}"
r = obj.isValid(s)
print(r)
