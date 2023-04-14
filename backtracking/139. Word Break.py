class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.back_tracking_method(s, wordDict)

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

    def back_tracking_method(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)
        import functools
        @functools.lru_cache(None)
        def back_track(s, start_idx: int, end_idx: int):
            ans = False
            for cur_idx in range(start_idx, end_idx + 1):
                if s[start_idx:cur_idx + 1] in word_dict:
                    if cur_idx == end_idx:
                        ans = True
                    else:
                        if back_track(s, cur_idx + 1, end_idx):
                            ans = True
            return ans

        return back_track(s, 0, len(s) - 1)







