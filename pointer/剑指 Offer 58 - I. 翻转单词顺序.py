class Solution:
    def reverse(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
        return s

    def reverseWords(self, s: str) -> str:
        li = s.split(' ')
        ss = []
        for e in li:
            if e == '':
                continue
            ss.append(e)

        temp = self.reverse(ss)
        return ' '.join(temp)