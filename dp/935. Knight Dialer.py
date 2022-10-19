class Solution:
    def knightDialer(self, n: int) -> int:
        #0<- 4,6 # can pass * and .... wtf
        # 1 <- 6,8
        # 2 <- 7,9
        # 3 <-4,8
        # 4 <-3,0,9
        #5 <-
        #6<-1,7,0
        #7<-2,6
        #8<-1,3
        #9<-2,4

        if n==1: return 10
        x=[1,1,1,1,1,0,1,1,1,1,]#init state
        for i in range(n-1):
            x=[
                x[4]+x[6],#0
                x[6]+x[8],#1,
                x[7]+x[9],#2,
                x[4]+x[8],#3,
                x[3]+x[0]+x[9],#4
                0,#5
                x[1]+x[7]+x[0],#6
                x[2]+x[6],#7
                x[1]+x[3],#8
                x[2]+x[4],#9
            ]
        return sum(x) % (10**9+7)