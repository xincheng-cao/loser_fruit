class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        left=0
        right =len(prices)-1
        revenue=0

        while left<right:
            if prices[left]<prices[right]:
                revenue=max(prices[right]-prices[left],revenue)
                if right-left>1:
                    if prices[left+1]<prices[left]:
                        left+=1
                    elif prices[right-1]>prices[right]:
                        right-=1
                    else:
                        if prices[left+1]-prices[left]>prices[right]-prices[right-1]:
                            right-=1
                        else:
                            left+=1
                else:
                    break
            else:
                revenue=max(0,revenue)
                if right-left>1:
                    if prices[left+1]<prices[left]:
                        left+=1
                    elif prices[right-1]>prices[right]:
                        right-=1
                    else:
                        if prices[left+1]-prices[left]>prices[right]-prices[right-1]:
                            right-=1
                        else:
                            left+=1
                else:
                    break
        return revenue
        '''
        if len(prices)<=1:
            return 0
        revenue=0
        min=prices[0]
        for i in range(1,len(prices)):
            if prices[i]-min>revenue:
                revenue=prices[i]-min
            if prices[i]<min:
                min=prices[i]
        return revenue