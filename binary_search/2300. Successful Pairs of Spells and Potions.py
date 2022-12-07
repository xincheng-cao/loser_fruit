class Solution:
    def successfulPairs(self, spells, potions, success: int):
        potions.sort()
        res = []

        for sp in spells:
            left = 0
            right = len(potions) - 1
            if potions[left] * sp >= success:
                res.append(len(potions))
                continue
            if potions[right] * sp < success:
                res.append(0)
                continue
            found = False
            while (left < right):
                mid = (left + right) // 2
                if potions[mid] * sp == success:
                    found = True
                    #res.append(len(potions) - mid)
                    break
                elif potions[mid] * sp > success:
                    right = mid - 1
                    continue
                else:
                    left = mid + 1
                    continue

            if found:
                temp=potions[mid]
                while(potions[mid]==temp):
                    ## bc there are dup....
                    mid-=1
                    if mid<0:
                        break
                res.append(len(potions)-mid-1)
                continue
            else:
                if left == right:
                    if left - 1 >= 0:
                        if potions[left - 1] * sp >= success:
                            res.append(len(potions) - left + 1)
                            continue
                    if potions[left] * sp >= success:
                        res.append(len(potions) - left)
                        continue
                    if potions[left + 1] * sp >= success:
                        res.append(len(potions) - left - 1)
                        continue
                else:  # right+1=left
                    if right - 1 >= 0:
                        if potions[right - 1] * sp >= success:
                            res.append(len(potions) - right + 1)
                            continue
                    if potions[right] * sp >= success:
                        res.append(len(potions) - right)
                        continue
                    res.append(len(potions) - left)
                    continue
        return res
