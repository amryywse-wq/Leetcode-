class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = len(nums2)-1
        k = len(nums1)-1
        temp = []
        if not nums1 and not nums2:
            return None
        elif not nums1 or m == 0:
            nums1[:] = nums2[:]
            return
        elif not nums2:
            return m, nums1
        while  j >= 0 and i>=0 :
            if nums2[j] >= nums1[i]:
                nums1[k] = nums2[j]
                
                k-= 1
                j-= 1
            elif nums2[j] <= nums1[i]:
                
                nums1[k] = nums1[i]
                i-=1
                k-=1
        if j >= 0:
            nums1[:j+1] = nums2[:j+1]
            
            
        
        m = m+n
        return m, nums1

p = Solution()
print(p.merge([4,5,0,0,0,0,0], 2, [1,2,3,5,6], 5))


            
            

            