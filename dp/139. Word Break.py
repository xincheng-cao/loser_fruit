class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)

        ans = [False] * len(s)

        for i in range(0, len(ans)):

            if s[:i + 1] in word_dict:
                ans[i] = True
                continue
            for j in range(0, i):
                if ans[j]:
                    # print(j,i+1,s[j:i+1])
                    if s[j + 1:i + 1] in word_dict:
                        ans[i] = True
                        break
        print(ans)
        return ans[-1]

