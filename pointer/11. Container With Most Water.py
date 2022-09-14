class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_area=(right-left)*min(height[left],height[right])

        while left<right:
            if right-left>1:
                if height[left]>height[right]:
                    right-=1
                    max_area=max(max_area,(right-left)*min(height[left],height[right]))
                else:
                    left+=1
                    max_area=max(max_area,(right-left)*min(height[left],height[right]))
            else:
                break
        return max_area