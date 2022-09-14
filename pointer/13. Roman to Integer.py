class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        MCMXCIV
        '''
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        left = 0
        right = 0
        s = list(s)
        ans = 0

        while left < len(s) and right < len(s):
            while (s[right] == s[left]):
                right += 1
                if right >= len(s): break
            num = (right - left) * dic[s[left]]
            if right >= len(s):
                ans += num
            else:
                if dic[s[left]] < dic[s[right]]:
                    num *= -1
                ans += num
            left = right
        return ans

