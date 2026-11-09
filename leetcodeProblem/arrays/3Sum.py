from itertools import islice as slice
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = []
    
        if len(nums) == 0 :
            return []
        sorted_val = sorted(nums)

       
        for i in range(len(sorted_val)-1) :
            right = len(sorted_val) -1
            left = i + 1

            if i > 0 and sorted_val[i] == sorted_val[i-1] :
                continue

            while left != right and left < right :
                total = sorted_val[left] + sorted_val[right]

                if total + sorted_val[i] != 0 :
                    if total + sorted_val[i] <= 0 :
                        left += 1
                    else :
                        right -= 1
                else :
                    ans.append([sorted_val[left], sorted_val[right], sorted_val[i]])

                    
                    

                    
                    

        return ans
                 


p = Solution()
print(p.threeSum([0,0,0,0,0,0])) 