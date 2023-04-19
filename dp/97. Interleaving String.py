class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):return False
        a=[False]*(len(s2)+1)
        #vec=[a[:]]*(len(s1)+1) !!wrong shallow copy
        vec=[]
        for i in range(len(s1)+1):
            vec.append(a[:])

        vec[0][0]=True

        for row in range(len(s1)+1):
            for col in range(len(s2)+1):
                s3_idx=row+col-1
                if row==0 and col==0:
                    continue
                if row==0:
                    if vec[row][col-1]==False:
                        vec[row][col]=False
                    else:
                        #move right
                        if s2[col-1]==s3[s3_idx]:
                            vec[row][col]=True
                        else:
                            vec[row][col]=False
                elif col==0:
                    if vec[row-1][col]==False:
                        vec[row][col]=False
                    else:
                        #move down
                        if s1[row-1]==s3[s3_idx]:
                            vec[row][col]=True
                        else:
                            vec[row][col]=False
                else:
                    if vec[row-1][col]==False and vec[row][col-1]==False:
                        vec[row][col]=False
                    elif vec[row-1][col] and vec[row][col-1]:
                        if s3[s3_idx]==s2[col-1] and s3[s3_idx]==s1[row-1]:
                            vec[row][col]=True
                        else:
                            vec[row][col]=False
                    elif vec[row-1][col]:
                        #move down
                        if s1[row-1]==s3[s3_idx]:
                            vec[row][col]=True
                        else:
                            vec[row][col]=False
                    elif vec[row][col-1]:
                        #move right
                        if s2[col-1]==s3[s3_idx]:
                            vec[row][col]=True
                        else:
                            vec[row][col]=False

                #print('\n',row,col)
                #for i in range(len(vec)):
                #    print(vec[i])
        return vec[-1][-1]





s1="bacc"
s2="aabcce"
s3="abaacbccec"

#s=Solution()
#print(s.isInterleave(s1,s2,s3))







