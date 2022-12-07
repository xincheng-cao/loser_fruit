# 有3条平行的、长度为n的路，每条路上有从0到n共n+1个点。一只青蛙从第二条路的0点出发、目的地到达n点。在3条路上可能会有一些障碍。
# 现在给一个长度为n+1的数组obstacles，来描述每个点上的障碍。obstacles[i]是一个0到3之间的整数，obstacles[i]=j表示在第j条路的i点有一个障碍（若j为0则说明i点在所有路上均无障碍）。
# 如果一条路的i+1点没有障碍，青蛙可以从这条路的i点移动到i+1点。除此之外，青蛙也可以横跳：从一条路的i点移动到另一条路（两条路未必相邻）的i点，如果新的路上i点没有障碍。
# 目标求青蛙跳到n点所需要的最少横跳次数。
# obstacles[0] == obstacles[n] == 0.
# 示例输入：Input: obstacles = [0,2,1,3,2,0], Output = 2; Input: obstacles = [0,1,3,1,3,0], Output = 0.

# ------
#   *
# ------
# F*  *
# ------
#    *
# ------
'''     col1    col2    col3    col4
row_0      1      1       ob      2
row_1     0       ob        2     2
row_2      1      1        1      1
'''

'''
lanes=[
    [...],
    [...],
    [...],
]

lanes[1][0]=0
lane[0][0] lanes[2][0] =0

i col j row
min_temp=100
for j in range(3):
    if lanes[j][i] is not 'ob':
        if lanes[j][i-1] is not 'ob':
            lanes[j][i]=lanes[j][i-1]
            if lane[j][i]<min_temp:
                min_temp=lane[j][i]
        else:
            lanes[j][i]=None
for j in range(3)
    if lanes[j][i] is None:
        lane[j][i]=min_temp+1

'''


def fn(obstacles: list) -> int:
    lanes_len = len(obstacles)
    lanes = [[0] * lanes_len] * 3

    col = 0
    for e in obstacles:
        if e > 0:
            lanes[e - 1][col] = -1
        col += 1

    lanes[0][0] = 1
    lanes[1][0] = 0
    lanes[2][0] = 1

    for col in range(1, lanes_len):

        min_temp = float('inf')
        for row in range(3):
            if lanes[row][col] != -1:
                if lanes[row][col - 1] != -1:
                    lanes[row][col] = lanes[row][col - 1]
                    if lanes[row][col] < min_temp:
                        min_temp = lanes[row][col]

        for row in range(3):
            if lanes[row][col] == 0:
                lanes[row][col] = min_temp + 1

    return min(lanes[0][-1], lanes[1][-1], lanes[2][-1])

# obstacles = [0,2,1,3,2,0], Output = 2
# time: O(n)
# space: O(n)->O(1)










