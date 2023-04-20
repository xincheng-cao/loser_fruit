class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        '''
        由于需要将数组分割成一个或多个由连续整数组成的子序列，因此只要知道子序列的最后一个数字和子序列的长度，就能确定子序列。
        哈希表的键为子序列的最后一个数字，值为最小堆，用于存储所有的子序列长度，最小堆满足堆顶的元素是最小的，因此堆顶的元素即为最小的子序列长度。
        '''
        import heapq
        last_element2len=dict()

        for e in nums:
            if e-1 in last_element2len:
                if len(last_element2len[e-1])==0:
                    if e in last_element2len:
                        heapq.heappush(last_element2len[e],1)
                    else:
                        last_element2len[e]=[1]
                else:
                    temp_shortest_len=heapq.heappop(last_element2len[e-1])
                    if e in last_element2len:
                        heapq.heappush(last_element2len[e],temp_shortest_len+1)
                    else:
                        last_element2len[e]=[temp_shortest_len+1]
            else:
                if e in last_element2len:
                    heapq.heappush(last_element2len[e],1)
                else:
                    last_element2len[e]=[1]
        for _,v in last_element2len.items():
            if len(v)==0:continue
            if v[0]<3:return False
        return True



