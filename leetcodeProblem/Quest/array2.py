class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_sum = sum(nums)
        n = len(nums)
        actual_sum = (n*(n+1)) / 2

        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                if actual_sum - nums_sum == 1:
                    return[nums[i], nums[i]+ 1]
                else :
                    return[nums[i], nums[i]-1]
            


        
                
            
            

p =Solution()
print(p.findErrorNums([3,2,2]))