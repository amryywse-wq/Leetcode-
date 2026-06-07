class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        i = 1 
        arr = []

        while i <=  n :
            if i % 3 == 0 and i % 5 == 0 :
                arr.append("FizzBuzz")
            
            elif i % 3 == 0 :
                arr.append("Fizz")

            elif i % 5 == 0:
                arr.append("Buzz")
            
            else :
                arr.append(str(i))

            i +=1
        
        return arr
    
p = Solution()
print(p.fizzBuzz(15))
