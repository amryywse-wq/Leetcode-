class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for num in nums[2:] :

            if arr1[len(arr1)-1] > arr2[len(arr2)-1] :
                insertPosArr1 = True
            else :
                insertPosArr1 =False

            if insertPosArr1 :
                arr1.append(num)
            else :
                arr2.append(num)

        return arr1 + arr2

p = Solution()
print(p.resultArray([5,4,3,8]))
        