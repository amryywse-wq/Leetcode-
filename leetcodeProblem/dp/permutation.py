class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        path = []

        def trace(path):

            if len(path) == len(nums) :
                ans.append(path)

            else :
                path_curr = {i:i for i in path}
                for ch in nums :
                    if ch not in path_curr :
                        trace(path+[ch])
                        
                     
                        
        trace(path)
    

        return ans

p = Solution()
print(p.permute([1]))

