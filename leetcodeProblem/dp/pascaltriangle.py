class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        pascalNum  = []
        for i in range(numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = pascalNum[i - 1][j-1] + pascalNum[i-1][j]

            pascalNum.append(row)
        
        return pascalNum
    


p = Solution()
print(p.generate(8))