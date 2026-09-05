class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left = 0 
        right = len(nums) -1
        indexes = []
        index_temp = 0

        while left <= right :
            
            mid = (left + right) // 2 
            
            while nums[mid] == target :
                mid =- 1
            
            if nums[mid+1] == target :
                mid += 1
                while nums[mid] == target :
                   indexes.append(mid) 
                   
            if nums[mid] > target :
                right = mid - 1
            else :
                left = mid + 1
            
        return indexes
    
p = Solution()
print(p.searchRange([1,1,2,2,4,4,5,5], 5))
            

                
