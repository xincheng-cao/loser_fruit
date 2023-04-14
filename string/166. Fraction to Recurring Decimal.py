class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        '''
        Input: numerator = 4, denominator = 333
        Output: "0.(012)"

        Input: numerator = 1, denominator = 2
        Output: "0.5"
        '''

        sign = '-'
        if numerator * denominator >= 0:
            sign = ''
        numerator = abs(numerator)
        denominator = abs(denominator)

        integer_part = numerator // denominator
        numerator = numerator % denominator

        decimal_part = '.'

        cur_pos = -1
        # 0 1 2 3 4 5 6 7 8 9 pos
        # 2 9 8 7 6 5 9 8 7 6 remainder
        #                     res
        res = []
        remainder2pos = dict()
        dejuva_pos = -1
        while numerator != 0:
            cur_pos += 1
            if numerator in remainder2pos:
                dejuva_pos = remainder2pos[numerator]
                break
            remainder2pos[numerator] = cur_pos
            numerator = numerator * 10
            res.append(
                str(numerator // denominator)
            )
            numerator = numerator % denominator

        if dejuva_pos != -1:
            res.insert(dejuva_pos, '(')
            res.append(')')

        if len(res) > 0:
            real_ans = sign + str(integer_part) + decimal_part + ''.join(res)
        else:
            real_ans = sign + str(integer_part) + ''.join(res)
        return real_ans
















