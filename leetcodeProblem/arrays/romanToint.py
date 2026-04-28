class Solution(object):
    def romanToInt(self, s):
        s = s.upper()
      
        val = []
        for w in s:
            if w == "I" :
                val.append(1)
            elif w == "V" :
                val.append(5)
            elif w == "X" :
                val.append(10)
            elif w == "L" :
                val.append(50)
            elif w == "C":
                val.append(100)
            elif w == "D":
                val.append(500)
            elif w == "M":
                val.append(1000)
        
        for i in range(len(val)):
            if val[i] < val[i+1 if i < len(val)-1 else i]:
                val[i] = val[i] * -1
        return sum(val)

p = Solution()
print(p.romanToInt("VII"))