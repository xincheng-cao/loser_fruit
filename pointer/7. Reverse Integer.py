class Solution:
    def reverse(self, x: int) -> int:

        flag = False
        if x < 0:
            x = abs(x)
            flag = True
        if x == 0:
            return 0

        s = str(x)
        cur = len(s) - 1
        while cur >= 0:
            if s[cur] == '0':
                cur -= 1
            else:
                break

        s = s[:cur + 1]
        left = 0
        right = len(s) - 1
        s = list(s)
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
        s = ''.join(s)
        if flag:
            s = '-' + s
        # 输出大于区间！！
        x = int(s)
        if x > pow(2, 31) - 1 or x < -1 * pow(2, 31):
            return 0
        return int(s)
