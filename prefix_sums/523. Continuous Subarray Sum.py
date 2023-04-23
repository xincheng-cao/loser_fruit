class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        from collections import OrderedDict

        prefix_sum=OrderedDict()
        prefix_sum[-1]=0
        pref_sum=0
        for i in range(len(nums)):
            pref_sum+=nums[i]
            prefix_sum[i]=pref_sum
        '''
        (n2*k+mod2)-(n1*k+mod1)=x
        if mod2==mod1 --> x%k==0
        '''

        remainder2idx=dict()
        remainder2idx[0]=-1
        for idx,sum in prefix_sum.items():
            remainder=sum%k
            if remainder not in remainder2idx:
                remainder2idx[remainder]=idx
            else:
                dist=idx-remainder2idx[remainder]
                if dist>=2:
                    return True
                else:
                    pass
                    # dont need to update remainder2idx bc the far the better
        return False