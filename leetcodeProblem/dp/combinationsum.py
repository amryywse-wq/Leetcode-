class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans= []
        path = []

        def trace(path, need):
            if need == 0 :
                exist = False
                path = sorted(path)
                for a in ans :
                    if a == path :
                        exist = True

                if not exist :
                    ans.append(path)

            elif need < 0 :
                return False

            for num in candidates :
                trace(path+[num], need - num)

        trace(path, target)
        
        return ans
                
    

p = Solution()
print(p.combinationSum([2,3,6,7],7))