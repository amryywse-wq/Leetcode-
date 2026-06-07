class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 3 and n > 0 :
            return True

        if n % 4 <=  3 and n > 4:
            return True
        else:
            return False 

p = Solution()
print(p.canWinNim(9))



        