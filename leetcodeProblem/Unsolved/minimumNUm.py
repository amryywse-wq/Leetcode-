class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """

        if len(word) < 8 :
            return len(word)

        ans = 0
        multiplier = len(word) // 8

        if multiplier == 1 :
            ans  = 8 + ((len(word) % 8) * 2)
        elif multiplier == 2 :
            ans = 24 + ((len(word) % 8) * 3)
        elif multiplier == 3 :
            ans = 48 + ((len(word) % 8) * 4)

        return ans, len("bvlqfomhxkpactrjunsidzey")

p = Solution()
print(p.minimumPushes("akmnbchfjue"))
