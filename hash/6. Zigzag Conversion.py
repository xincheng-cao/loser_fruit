class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = dict()
        for i in range(numRows):
            res[i] = []

        while len(s) > 0:
            win_len = (numRows - 1) * 2
            left = s[:win_len]
            right = s[win_len:]
            for i in range(numRows - 1):
                if len(left) >= i + 1:
                    res[i].append(left[i])
            for i in range(numRows - 1):
                if len(left) >= i + numRows - 1 + 1:
                    res[numRows - 1 - i].append(left[i + numRows - 1])
            s = right
        real_res = ''
        for i in range(numRows):
            real_res += ''.join(res[i])
        return real_res