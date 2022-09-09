class Solution:
    def trap(self, height: List[int]) -> int:
        mon_stack=[]
        mon_stack.append(0)
        ans=0

        for i in range(1,len(height)):
            if height[i]<=height[mon_stack[-1]]:
                mon_stack.append(i)
            else:
                while mon_stack.__len__()>0 and height[mon_stack[-1]]<height[i]:
                    base_idx=mon_stack.pop()
                    if mon_stack.__len__()==0:
                        break
                    left_wall_idx=mon_stack[-1]
                    # debug here: i-base_idx is wrong its actually i- left_wall_idx
                    width=i-left_wall_idx-1
                    right_wall_idx=i
                    temp_height=min(height[left_wall_idx],height[right_wall_idx])-height[base_idx]
                    ans+=temp_height*width
                mon_stack.append(i)
        return ans



    '''
    # cant solve height=[10,8,6,4,2,1,3,5,4,4,7,3,4,5]
    def trap(self, height: List[int]) -> int:
        mon_stack=[]
        mon_stack.append(0)
        ans=0

        for i in range(1,len(height)):
            if mon_stack.__len__()==0:
                mon_stack.append(i)
            elif mon_stack.__len__()==1:
                if height[mon_stack[0]]<=height[i]:
                    mon_stack.pop()
                    # need push i in monstack
                    mon_stack.append(i)
                else:
                    mon_stack.append(i)
            else:
                if height[i]<=height[mon_stack[-1]]:
                    mon_stack.append(i)
                else:
                    min_height_idx=mon_stack[-1]
                    mon_stack.append(i)
                    while(i+1<len(height)):
                        if height[i+1]>=height[i]:
                            i+=1
                            mon_stack.append(i)
                        else:
                            break
                    width=i-mon_stack[0]-1
                    if height[i]>=height[mon_stack[0]]:
                        max_height_idx=mon_stack[0]
                    else:
                        max_height_idx=i
                    ans+=width*(height[max_height_idx]-height[min_height_idx])
                    for j in range(1,len(mon_stack)-1):
                        # caution dont forget to subtract height[min_height_idx]
                        ans-=((height[mon_stack[j]]-height[min_height_idx])*1)
                    # mon_stack=[] this is wrong
                    mon_stack=[mon_stack[-1]]
        return ans
    '''