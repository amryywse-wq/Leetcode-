class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permuted = [nums]
        
        arrLen = len(nums)

        def count_permutation(tempArr):
            n = arrLen
            tempNum = 0
            #while n > 1 :
            