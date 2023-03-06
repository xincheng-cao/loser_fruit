class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        def get_max(c: str, ):
            left = 0
            right = 0
            if answerKey[left] == c:
                count_c = 1
            else:
                count_c = 0
            # bc k>=1
            max_len = right - left + 1

            while left < len(answerKey) - 1 and right < len(answerKey) - 1:
                if count_c > k:
                    if left == right:
                        left += 1
                        right += 1
                        if answerKey[left] == c:
                            count_c = 1
                        else:
                            count_c = 0
                    else:
                        if answerKey[left] == c:
                            count_c -= 1
                            left += 1
                        else:
                            left += 1
                elif count_c < k:
                    right += 1
                    if answerKey[right] == c:
                        count_c += 1
                    if right - left + 1 > max_len:
                        max_len = right - left + 1
                else:
                    right += 1
                    if answerKey[right] == c:
                        count_c += 1
                    else:
                        if right - left + 1 > max_len:
                            max_len = right - left + 1
            return max_len

        return max(get_max('T'), get_max('F'))







