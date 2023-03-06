class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        # max(plants[i]) <= capacityA, capacityB <= 109

        left = -1
        right = len(plants)
        ans = 0
        cur_left = capacityA
        cur_right = capacityB
        while right - left >= 2:
            if left + 1 == right - 1:
                if cur_left < plants[left + 1] and cur_right < plants[left + 1]:
                    ans += 1

                break

            if cur_left < plants[left + 1]:
                ans += 1
                cur_left = capacityA
            if cur_right < plants[right - 1]:
                ans += 1
                cur_right = capacityB
            cur_left = cur_left - plants[left + 1]
            cur_right = cur_right - plants[right - 1]
            left += 1
            right -= 1
        return ans



