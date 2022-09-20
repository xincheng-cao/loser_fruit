class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        haystack_len = len(haystack)

        dic = dict()
        for i in range(0, haystack_len - needle_len + 1):
            sub_str = haystack[i:i + needle_len]
            if sub_str in dic:
                continue
            else:
                dic[sub_str] = i

        if needle not in dic:
            return -1
        else:
            return dic[needle]
