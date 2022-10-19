class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n_list = list(str(n))
        if len(n_list) <= 1:
            return -1
        '''
        if len(n_list)==2:
            if int(n_list[1]+n_list[0])>n:
                return int(n_list[1]+n_list[0])
            else:
                return -1
        '''
        right = len(n_list) - 2
        while right >= 0:
            if n_list[right] < n_list[right + 1]:
                break
            else:
                right -= 1
        if right == -1: return -1
        right_right = len(n_list) - 1
        while right_right > right:
            if n_list[right_right] > n_list[right]:
                break
            else:
                right_right -= 1
        if n_list[right_right] <= n_list[right]:
            return -1

        temp = n_list[right]
        n_list[right] = n_list[right_right]
        n_list[right_right] = temp

        # reverse right+1 ~ len(n_list)-1
        left = right + 1
        right = len(n_list) - 1
        while (left < right):
            temp = n_list[left]
            n_list[left] = n_list[right]
            n_list[right] = temp
            left += 1
            right -= 1

        res = int(''.join(n_list))
        if res >= 2 ** 31:
            return -1

        return res
