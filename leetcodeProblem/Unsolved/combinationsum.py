class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candDict = {can : can for can in candidates}

        return candDict


p = Solution()
print(p.combinationSum([1,2,3,4],7))