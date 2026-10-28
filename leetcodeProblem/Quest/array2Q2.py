#Brute Force

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        ans = []
        for i in nums:
            for j in nums:
                if i > j :
                    count += 1

            ans += [count]
            count = 0

        return ans

p = Solution()
print(p.smallerNumbersThanCurrent([8,1,2,2,3]))