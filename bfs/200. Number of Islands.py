class Solution:
    '''
    def dfs(self,grid,i,j):
        grid[i][j]='0'
        if i>=1:
            above=grid[i-1][j]
            if above=='1':
                self.dfs(grid,i-1,j)
        if i<len(grid)-1:
            below=grid[i+1][j]
            if below=='1':
                self.dfs(grid,i+1,j)
        if j>=1:
            left=grid[i][j-1]
            if left=='1':
                self.dfs(grid,i,j-1)
        if j<len(grid[0])-1:
            right=grid[i][j+1]
            if right=='1':
                self.dfs(grid,i,j+1)

    def numIslands(self, grid: List[List[str]]) -> int:
        ans=0
        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    ans+=1
                    self.dfs(grid,i,j)
        return ans
    '''
    # bfs
    def numIslands(self, grid: List[List[str]]) -> int:
        ans =0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    ans+=1

                    # bfs
                    que=[]
                    que.insert(0,(i,j))
                    grid[i][j]='0'
                    while len(que)>0:
                        i1,j1=que.pop()
                        #grid[i1][j1]='0'
                        # if you set zero here it will timeout

                        if i1>=1:
                            if grid[i1-1][j1]=='1':
                                grid[i1-1][j1]='0'
                                que.insert(0,(i1-1,j1))
                        if i1<len(grid)-1:
                            if grid[i1+1][j1]=='1':
                                grid[i1+1][j1]='0'
                                que.insert(0,(i1+1,j1))
                        if j1>=1:
                            if grid[i1][j1-1]=='1':
                                grid[i1][j1-1]='0'
                                que.insert(0,(i1,j1-1))
                        if j1<len(grid[0])-1:
                            if grid[i1][j1+1]=='1':
                                grid[i1][j1+1]='0'
                                que.insert(0,(i1,j1+1))
        return ans
