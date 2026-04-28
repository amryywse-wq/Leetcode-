class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        removeCh = {" ", ".", ",", ":", "'"}
        newString = ("".join(wrd for wrd in s if wrd not in removeCh)).upper()
        if not newString or len(newString) == 1:
            return True
        i = 0
        j = len(newString)-1

        while i >=0 and  j > i:
            if newString[i] == newString[j]:
                i+=1
                j-=1
            else:
                return False, newString
        return newString, True    
        
        
        

print(Solution().isPalindrome("abb"))    
