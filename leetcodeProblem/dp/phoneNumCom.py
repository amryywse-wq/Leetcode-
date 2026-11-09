class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digits = str(digits)

        phone_board = {
                '1': [],                '2': ['a', 'b','c'],    '3': ['d','e','f'],
                '4': ['g','h','i'],     '5': ['j','k','l'],     '6': ['m','n','o'],
                '7': ['p','q','r','s'], '8': ['t','u','v'],     '9': ['w','x','y','z']
            }

        
        ans = []
        path = ''
        indx = [i for i in digits]

        def trace(path, indx, i):
            if i == len(indx)-1 :
                for val in phone_board[indx[i]] :
                    ans.append(path+val)
                
            else :
                for val in phone_board[indx[i]]:
                    trace(path+val, indx, i+1)

        trace(path, digits, 0)

        return ans



p = Solution()
print(p.letterCombinations(digits='2367'))
