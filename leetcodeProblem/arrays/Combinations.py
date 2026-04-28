class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        temp = target
        ans = []
        tempAns = []
        i = 0
        val = "exist"
        key = dict.fromkeys(candidates, val)
        while i < len(candidates) :
            if temp < 0 :
                temp = target
                tempAns =[]
                i+=1
            elif target == candidates[i]:
                ans.append([candidates[i]])
                i+=1
            else :
                temp = temp - candidates[i]
                tempAns.append(candidates[i])
                if temp in key :
                    tempAns.append(temp)
                    ans.append(tempAns)
                    tempAns =[]
                    temp = target
                    i+=1
                

        
        return ans
                    
                
            

p = Solution()
print(p.combinationSum([1,2,3,4,5,8], 7))                

                    
            
                
                          
                
            
