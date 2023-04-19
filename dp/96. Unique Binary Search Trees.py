class Solution:
    def numTrees(self, n: int) -> int:
        len2count=dict()
        len2count[0]=1
        len2count[1]=1

        for whole_len in range(2,n+1):
            temp_sum=0
            for root_idx in range(1,whole_len+1):
                left_len=root_idx-1
                right_len=whole_len-root_idx
                temp_sum+=(len2count[left_len]*len2count[right_len])
            len2count[whole_len]=temp_sum
        return len2count[n]

