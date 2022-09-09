
def trap( height) -> int:
    ans = 0
    stack = list()
    n = len(height)

    for i, h in enumerate(height):
        while stack and h > height[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            left = stack[-1]
            currWidth = i - left - 1
            currHeight = min(height[left], height[i]) - height[top]
            ans += currWidth * currHeight
        stack.append(i)

    return ans

height=[10,8,6,4,2,1,3,5,4,4,7,3,4,5]
trap(height)
