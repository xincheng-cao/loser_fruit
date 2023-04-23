class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:return 0

        str_set = set()
        max_len = float('-inf')

        left = 0
        right = 0
        max_len = 1
        str_set.add(s[left])
        while right < len(s):
            if right == len(s) - 1:
                break
            while s[right + 1] not in str_set:
                right += 1
                str_set.add(s[right])
                max_len = max(max_len, len(str_set))
                if right +1 >=len(s):
                    break
            if right+1>=len(s):
                break
            tgt = right + 1

            while left <= tgt:

                if s[left] == s[tgt]:
                    str_set.remove(s[left])
                    left += 1
                    break
                else:

                    str_set.remove(s[left])
                    left += 1
            right = tgt
            if right<len(s):
                str_set.add(s[right])
                max_len = max(max_len, len(str_set))
        return max_len

#s=Solution()
#s.lengthOfLongestSubstring('abcabcbb')