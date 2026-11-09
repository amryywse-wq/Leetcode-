class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        i = 0
        j = i+1

        while j < len(nums):
            while nums[j] < nums[i] and i >= 0:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                temp = ''

                j = i
                i -= 1


            i += 1
            j = i + 1
    

            
        return nums


p = Solution()
print(p.sortColors([2,0,2,1,1,0]))
                

            
            
                    
                            