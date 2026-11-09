class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        hash_map = {num : num for num in nums}

        for i in range(1, len(nums)+1):
            if i not in hash_map :
                ans.append(i)
            
        return ans


p = Solution()
print(p.findDisappearedNumbers([4,3,2,7,8,2,3,1,9,9]))  