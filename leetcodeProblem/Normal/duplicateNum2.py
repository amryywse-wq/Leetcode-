class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_length = len(nums)
        k=2
        i=0
        while i < len(nums):
            if nums[i] != '_' and i < len(nums)-2 :
                if nums[i] != nums[k]:
                    if nums[i] == nums[i+1]:
                        i = k
                        k += 2
                    else :
                        i +=1
                        k += 1
                else:
                    del nums[i]
                    
            else :
                return len(nums), nums

                    
            
p = Solution()
print(p.removeDuplicates([0,0,0,0,1,1,2,3,3,3,4,4,4,4,4]))        

