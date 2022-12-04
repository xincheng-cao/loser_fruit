class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word2num = dict()
        for e in words:
            if e in word2num:
                word2num[e] += 1
            else:
                word2num[e] = 1

        res = 0
        keys = list(word2num.keys())

        for e in keys:
            if word2num[e] > 0:
                if e[0] == e[1]:
                    if word2num[e] // 2 >= 1:
                        res += (word2num[e] // 2) * 2
                        word2num[e] -= (word2num[e] // 2) * 2
                else:
                    f = e[1] + e[0]
                    if f in word2num:
                        if word2num[f] > 0:
                            temp_min = min(word2num[f], word2num[e])
                            res += temp_min * 2
                            word2num[f] -= temp_min
                            word2num[e] -= temp_min

        for e in keys:
            if word2num[e] > 0 and e[0] == e[1]:
                res += 1
                break
        return res * 2