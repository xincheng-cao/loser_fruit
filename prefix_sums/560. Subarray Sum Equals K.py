'''
from collections import OrderedDict
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        prefix_dict=OrderedDict()
        prefix_dict[-1]=0
        ans=0

        for i in range(0,len(nums)):
            prefix_dict[i]=prefix_dict[i-1]+nums[i]
        reverse_dict=dict()
        for kk,v in prefix_dict.items():
            if v not in reverse_dict:
                reverse_dict[v]=[kk]
            else:
                reverse_dict[v].append(kk)

        for right in range(len(nums)):
            #print(prefix_dict[right],k)
            left_val=prefix_dict[right]-k
            if left_val in reverse_dict:

                for idx in reverse_dict[left_val]:
                    if idx<right:
                        ans+=1


        return ans



'''

from collections import OrderedDict


class Solution:
    def subarraySum(self, nums, k: int) -> int:
        prefix_dict = OrderedDict()
        prefix_dict[-1] = 0
        reverse_dict = dict()
        reverse_dict[0] = [-1]
        ans = 0

        for right in range(len(nums)):
            # print(prefix_dict[right],k)
            prefix_dict[right] = prefix_dict[right - 1] + nums[right]

            left_val = prefix_dict[right] - k
            if left_val in reverse_dict:
                ans += len(reverse_dict[left_val])
            if prefix_dict[right] in reverse_dict:
                reverse_dict[prefix_dict[right]].append(right)
            else:
                reverse_dict[prefix_dict[right]] = [right]

        return ans



