class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ans = []

        for i in range(len(tokens)) :
            if tokens[i] == "+" :
                a = ans.pop()
                b = ans.pop()
                calc = b + a 
                ans.append(calc)
            elif tokens[i] == "-" :
                a = ans.pop()
                b = ans.pop()
                calc = b - a 
                ans.append(calc)                    
            elif tokens[i] == "*" :
                a = ans.pop()
                b = ans.pop()
                calc = b * a 
                ans.append(calc)
            elif tokens[i] == "/" :
                a = ans.pop()
                b = ans.pop()
                calc = int(b / a) 
                ans.append(calc)
            else :
                ans.append(int(tokens[i]))

        return ans[0]

p = Solution()
print(p.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))