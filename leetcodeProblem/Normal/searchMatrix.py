class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def searchPos(matrix):
            search = int(len(matrix)/2)

            if target > matrix[search][len(matrix[search])-1] :
                matrix = matrix[search:]

                searchPos(matrix)

            elif matrix[search][0] <= target and target <= matrix[search][len(matrix[search])-1]:
                for i in range(len(matrix[search])):
                    if matrix[search][i] == target :
                        return True
                    else :
                        return False
            else :
                matrix = matrix[:search]
                searchPos(matrix)
            
            
           
        
        res = searchPos(matrix)

        return res

p = Solution()
print(p.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],0))
