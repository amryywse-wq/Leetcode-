class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        def count(strr):  
            pair =[]
            cnt = 0
            if strr == '1' :
                return opn([['1','1']])
            else:    
                for i in range(len(strr)-1):
                    cnt += 1
                    if strr[i] != strr[i+1] :
                        pair =  pair + [[str(cnt), strr[i]]]
                        cnt = 0


                if strr[len(strr)-1] != strr[len(strr)-2]:
                    pair = pair + [['1', strr[len(strr)-1]]]
                else :
                    pair =  pair + [[str(cnt+1), strr[len(strr)-1]]]


            return opn(pair)
                
        def opn(arr):
            strr = ''
            for elem in arr :
                for num in elem :
                    strr += num
            return strr

        for i in range(1, n+1):
            if i == 1 :
                strr = '1'
            else :
                strr = count(strr)

            print(i)


    
        return strr

        
            

p = Solution()
print(p.countAndSay(10))