class Solution2(object):
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                ans=[]
                for t in s.split(c):
                    ans.append(self.longestSubstring(t, k))
                return max(ans)
        return len(s)



class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        def dfs(s: str, kkkk: int):
            if len(s) < kkkk:
                return 0

            ch2count = dict()
            for ch in s:
                if ch in ch2count:
                    ch2count[ch] += 1
                else:
                    ch2count[ch] = 1
            ans=len(s)
            for ch,v in ch2count.items():
                if v<kkkk:
                    sub_s_list=s.split(ch)
                    temp=[]
                    for sub in sub_s_list:
                        temp.append(
                            dfs(sub,kkkk)
                        )
                    ans=max(temp)
                    break#important here!!!!
            return ans



        return dfs(s, k)


st="aaaaaaaaaaaabcdefghijklmnopqrstuvwzyz"
k=3
'''
"aaaaaaaaaaaabcdefghijklmnopqrstuvwzyz"
3
'''

s=Solution()
print(s.longestSubstring(st,k))