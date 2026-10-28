from random import random as rand
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        

        alphabet = {chr(i): int(int(i) * rand()) if int(i) % 2 == 0 else int(i) for i in range(ord('a'),ord('z') + 9)}
        res = {}
        total = 0
        for str in strs :
            for i in range(len(str)):
                total += alphabet[str[i]]

            if total not in res :
                res[total] = [str]
                total = 0
            else :
                res[total] += [str]
                total = 0

        return [val for val in res.values()], alphabet.items()

                
                            
   
p = Solution()
print(p.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    