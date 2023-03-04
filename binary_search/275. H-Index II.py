class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left=0
        right= len(citations)-1

        while left<=right:
            mid=(left+right)//2

            num_paper=len(citations)-mid
            if num_paper<=citations[mid]:
                right=mid-1
            else:
                left=mid+1
        return len(citations)-left
