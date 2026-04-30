class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True

        elif n == 0 :
            return False
        
        def recur(n):
            if n % 2 == 0 :
                return recur(n // 2)
            
            return n
            
                        
        p = recur(n)

        if p == 1:
            return True
        else :
            return False

        
        
        
        
            
        
    
        

    

p = Solution()
print(p.isPowerOfTwo(23))




