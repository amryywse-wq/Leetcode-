class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """ 
        def factorial(num):
            total = 1 
            while num > 0 :
                total = total * num
                num -= 1

            return total
        #Using Comnbination Count how many possible paths
        return factorial(m+n-2)//(factorial(m-1)*factorial(n-1))



p = Solution()
print(p.uniquePaths(1,1))

            