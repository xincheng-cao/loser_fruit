class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        idx2len = dict()
        longest = float('-inf')
        for idx in nums:
            if idx in idx2len: continue

            # idx-1, idx, idx+1
            if idx - 1 in idx2len:
                idx_minus1_2_len = idx2len[idx - 1]
            else:
                idx_minus1_2_len = 0

            if idx + 1 in idx2len:
                idx_plus1_2_len = idx2len[idx + 1]
            else:
                idx_plus1_2_len = 0

            if idx_minus1_2_len == 0 and idx_plus1_2_len == 0:
                cur_len = 1
                idx2len[idx] = 1
            elif idx_minus1_2_len != 0 and idx_plus1_2_len != 0:
                cur_len = idx_minus1_2_len + 1 + idx_plus1_2_len
                idx2len[idx - idx_minus1_2_len] = cur_len
                idx2len[idx + idx_plus1_2_len] = cur_len
                idx2len[idx] = cur_len  # easy to forget!!
            elif idx_minus1_2_len != 0:
                cur_len = idx_minus1_2_len + 1
                idx2len[idx - idx_minus1_2_len] = cur_len
                idx2len[idx] = cur_len
            else:
                cur_len = idx_plus1_2_len + 1
                idx2len[idx + idx_plus1_2_len] = cur_len
                idx2len[idx] = cur_len

            if cur_len > longest: longest = cur_len
        return longest

