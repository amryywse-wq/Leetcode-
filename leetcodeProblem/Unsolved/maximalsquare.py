class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 1 and len(matrix[0]) == 1 :
            return int(matrix[0][0])
        maxVal = 0

        for ar in range(len(matrix)-1):
            for i in range(len(matrix[ar])-1):
                valCheck = int(matrix[ar][i]) + int(matrix[ar][i+1]) + int(matrix[ar+1][i]) + int(matrix[ar+1][i+1])
             
                if valCheck >= maxVal :
                    maxVal = valCheck

        if len(matrix) <= 2 and maxVal > 0 :
            return 1   
        
        return maxVal
        


        
p = Solution()
print(p.maximalSquare([["1","0"]]))