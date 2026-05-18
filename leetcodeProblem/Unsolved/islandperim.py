class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perim = 0 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 :
                    perim += 4
                    if  i == 0 and j < len(grid[i])-1 and j > 0:
                        if grid[i+1][j] == 1 :
                            perim -= 1
                        if grid[i][j-1] == 1 :
                            perim -= 1
                        if grid[i][j+1] == 1:
                            perim -= 1

                        print("total = ", perim, "at = ", i, j)
                        

                    if i == len(grid)- 1 and j < len(grid[i])-1 and j > 0:
                        if grid[i-1][j] == 1 :
                            perim -= 1
                        if grid[i][j-1] == 1 :
                            perim -= 1
                        if grid[i][j+1] == 1:
                            perim -= 1

                        print("total = ", perim, "at = ", i, j)

                    if j == 0 and i == 0 and len(grid) > 1:
                        if grid[i][j+1] == 1 :
                            perim -= 1
                        if grid[i+1][j] == 1 :
                            perim -=1
                        
                        print("total = ", perim, "at = ", i, j)
                        
                    if j == len(grid[i]) -1 and i == 0 and len(grid) > 1:
                        if grid[i][j-1] == 1 :
                            perim -= 1
                        if grid[i+1][j] == 1 :
                            perim -= 1

                        print("total = ", perim, "at = ", i, j)

                    if j == 0 and i == len(grid) - 1 and len(grid) > 1:
                        if grid[i-1][j] == 1 :
                            perim -= 1
                        if grid[i][j+1] == 1 :
                            perim -= 1

                        print("total = ", perim, "at = ", i, j)
                    
                    if j == len(grid[i]) - 1 and i == len(grid) -1 and len(grid) > 1:
                        if grid[i-1][j] == 1 :
                            perim -= 1
                        if grid[i][j-1] == 1 :
                            perim -= 1
                        
                        print("total = ", perim, "at = ", i, j)
                    
                    if j == 0 and i > 0 and i < len(grid)-1 and len(grid) > 1 :
                        if grid[i][j+1] == 1:
                            perim -= 1
                        if grid[i+1] == 1:
                            perim -= 1
                        if grid[i-1][j] == 1:
                            perim -= 1

                        print("total = ", perim, "at = ", i, j)
                    
                    if j == len(grid[i])-1 and i > 0 and i < len(grid)-1 and len(grid) > 1 :
                        if grid[i][j-1] == 1:
                            perim -= 1
                        if grid[i+1][j] == 1:
                            perim -= 1
                        if grid[i-1][j] == 1 :
                            perim -= 1
                        
                        print("total = ", perim, "at = ", i, j)

                    if i > 0 and i < len(grid)-1 and j > 0 and j < len(grid[i]) -1:
                        if grid[i][j+1] == 1 :
                            perim -= 1
                        if grid[i][j-1] == 1 :
                            perim -= 1
                        if grid[i+1][j] == 1 :
                            perim -= 1
                        if grid[i-1][j] == 1 :
                            perim -= 1

                        print("total = ", perim, "at = ", i, j)
                    
        return perim
    



p = Solution()
print(p.islandPerimeter([[1,1]]))
