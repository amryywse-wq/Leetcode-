class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        sorted_list = sorted(strs)
        first_word = sorted_list[0]
        last_word = sorted_list[len(sorted_list)-1]
        prefix = ""

        for i in range(len(first_word)):
            if first_word[i] == last_word[i]:
                prefix = prefix + first_word[i]
            else:
                return prefix
        
        return prefix