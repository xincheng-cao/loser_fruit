import math


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        # 2^20 + 2^20 = 2^21
        # 0 <= deliciousness[i] <= 220
        ans = 0
        two_power_list = [1]
        for i in range(1, 22):
            two_power_list.append(two_power_list[-1] * 2)

        dic_deli = dict()
        for e in deliciousness:
            if e not in dic_deli:
                dic_deli[e] = 1
            else:
                dic_deli[e] += 1

        for e in deliciousness:
            for sum in two_power_list:
                sub = sum - e
                if sub == e and dic_deli[sub] >= 2:
                    ans += (dic_deli[sub] - 1)
                    # print(sub,e)
                elif sub in dic_deli:
                    if dic_deli[sub] >= 1 and sub != e:
                        ans += (dic_deli[sub])
                        # print(sub,e)
            dic_deli[e] -= 1
        return ans % int(math.pow(10, 9) + 7)
