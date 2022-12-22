class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left,right):
            if left+right==2*n:
                return []
            if left==right and left<n:
                temp_res=dfs(left+1,right)
                for i in range(len(temp_res)):
                    temp_res[i]='('+temp_res[i]
                return temp_res
            if left==n:
                return [')'*(n-right)]
            temp_res0=dfs(left+1,right)
            temp_res1=dfs(left,right+1)
            for i in range(len(temp_res0)):
                temp_res0[i]='('+temp_res0[i]
            for i in range(len(temp_res1)):
                temp_res1[i]=')'+temp_res1[i]
            return temp_res0+temp_res1
        return dfs(0,0)

