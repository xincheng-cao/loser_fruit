class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction=0
        # 0 N
        # 1 E
        # 2 S
        # 3 W
        x=0
        y=0

        for i in range(4):
            for s in instructions:
                if s=='R':
                    direction+=1
                elif s=='L':
                    direction-=1
                else:
                    if direction %4 ==0:
                        y+=1
                    elif direction%4==1:
                        x+=1
                    elif direction%4==2:
                        y-=1
                    else:
                        x-=1
            if x==0 and y==0:return True
        if x==0 and y==0:return True
        return False
