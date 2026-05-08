class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        if len(grid) == 1 :
            for land in grid[0] :
                if land == "1":
                    count += 1
            
            return count
        
        else :
            for i in range(len(grid)-1):
                for j in range(len(grid[i])):
                    if grid[i][j] == grid[i+1][j+1]:
                        temp = 1



p = Solution()
print(p.numIslands([["0","0","0","0","0","1"]]))