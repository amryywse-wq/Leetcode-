class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        
        ballooon = {'b': 0, 'a' : 0, 'l': 0,'o' : 0, 'n' : 0  }

        for chr in text :
            if chr in ballooon :
                ballooon[chr] += 1
        
        if ballooon['l'] < 2 or ballooon['o'] < 2: 
            total = 0
        else :
            if ballooon['l'] > ballooon['o'] :
                subTotal = ballooon['o'] // 2
            else :
                subTotal = ballooon['l'] // 2

            total = min(subTotal,min(ballooon.values()))

        return total

p = Solution()
inst = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
print(p.maxNumberOfBalloons(inst))



        