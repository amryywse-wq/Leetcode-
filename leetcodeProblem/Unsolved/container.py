class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        avr = sum(height)/len(height)
        k = len(height)-1
        max = 0
        for i in range(int(len(height)/2)+1):
            if height[i] >= avr:
                while k > i:
                    if height[i] > height[k]:
                        trHeight = height[k]
                    else:
                        trHeight = height[i]
                    
                    new_max = trHeight * (len(height)-i-(len(height)-k))
                    
                    if new_max > max :
                        max = new_max
                        k=k-1
                    else :
                        k=k-1
                
                k = len(height)-1
           
        
        return max, trHeight, avr, i
    

p = Solution()
print(p.maxArea([8,1,1,1,1,1,7,1]))
