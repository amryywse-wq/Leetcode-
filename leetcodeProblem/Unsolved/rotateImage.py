class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rotatedMatrix = [[0] * len(matrix) ] * len(matrix) 

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
              rotatedMatrix[j][j-(1+i)] = matrix[i][j] 

        return rotatedMatrix





p = Solution()
print(p.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))