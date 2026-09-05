class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        for str in s :
            if str == '*' and len(result) != 0 :
                result = result[:len(result)-1]
            
            elif str == '#' and len(result) != 0 :
                result = result + result

            elif str == '%' and len(result) != 0 :
                result = result[::-1]
            
            elif str != '%' and str != '#' and str != '*' and str.lower() == str :
                result = result + str
            
            else :
                result = result
            


        return result
    

p = Solution()
print(p.processStr(""))


