class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        left=0
        right=0
        _set=set()
        _set.add(s[left])
        max_len=1
        # missing right<len(s)-1
        while left<=right and right<len(s)-1:
            right+=1
            if s[right] not in _set:
                _set.add(s[right])
                max_len=max(max_len,right-left+1)
                continue
            else:
                while (left<right):
                    _set.remove(s[left])
                    left+=1
                    if s[right] in _set:
                        continue
                    else:
                        _set.add(s[right])
                        max_len=max(max_len,right-left+1)
                        break
        return max_len
