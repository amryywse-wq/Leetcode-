class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []
        for char in s :
            if char in parentheses.keys():
                stack.append(char)
                
            else:
                if not stack :
                    return False, "here", stack, char
                top = stack.pop()
                if parentheses.get(top) != char:
                    return False, "there", stack
        
        return not(stack)
print(Solution().isValid("(]"))
