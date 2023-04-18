class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        非负整数
        '''
        if num2 == '0' or num1 == '0': return '0'

        add_list = []
        for i1 in range(len(num1) - 1, -1, -1):
            x1 = int(num1[i1])
            temp_ans = ''
            adv = 0
            for i2 in range(len(num2) - 1, -1, -1):
                x2 = int(num2[i2])
                temp_ans = str((x1 * x2 + adv) % 10) + temp_ans
                adv = (x1 * x2 + adv) // 10

            if adv != 0:
                temp_ans = str(adv) + temp_ans
            add_list.append(temp_ans)

        for i in range(len(add_list)):
            add_list[i] = add_list[i] + '0' * i

        # print(add_list)
        max_len = float('-inf')
        for i in range(len(add_list)):
            if len(add_list[i]) > max_len:
                max_len = len(add_list[i])

        for i in range(len(add_list)):
            add_list[i] = '0' * (max_len - len(add_list[i])) + add_list[i]

        real_ans = ''
        adv = 0
        for col in range(max_len - 1, -1, -1):
            temp_ans = adv
            for row in range(len(add_list)):
                temp_ans += int(add_list[row][col])
            real_ans = str(temp_ans % 10) + real_ans
            adv = temp_ans // 10
        if adv != 0:
            real_ans = str(adv) + real_ans
        return real_ans




