class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candDict = {can : can for can in candidates}

        count = target
        tempAns = []
        ans = []
        for num in candidates:
            while count > 0 :
                count -= num
                tempAns.append(num)
                if count in candDict :
                    tempAns.append(candDict)
                    ans.append(tempAns)
                    count = target
                


p = Solution()
print(p.combinationSum([1,2,3,4],7))