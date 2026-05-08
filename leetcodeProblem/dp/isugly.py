class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        prime = []

        c = 2 
        
        while c * c <= n :
            while n % c == 0:
                if c <= 5 :
                    prime.append(c)
                    n //= c
                else:
                    return False
                
            c +=1
        
        if n > 5 :
            return False

        return True
    

p = Solution()
print(p.isUgly())