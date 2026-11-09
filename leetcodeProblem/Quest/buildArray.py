class Solution(object):
    def buildArray(target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """

        ans = []
        for i in range(len(target)):
            cnt = 0
            if i == 0 :
                while i < target[0]-1 :
                    i += 1
                    ans.append("Push")
                    cnt += 1

                while cnt > 0 :
                    ans.append("Pop")
                    cnt -= 1

                ans.append("Push")
                cnt = 0
                continue
            
            for j in range(target[i-1]+1, target[i]+1):
                if j != target[i] :
                    ans.append("Push")
                    cnt += 1

                else :
                    while cnt > 0 :
                        ans.append("Pop")
                        cnt -= 1

                    ans.append("Push")
                
        return ans


p = Solution
print(p.buildArray([3,5,7], 8))

             
            
            
            
