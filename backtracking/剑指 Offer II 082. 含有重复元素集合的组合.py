class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        tree=[]
        num2len=dict()
        for e in candidates:
            if e in num2len:
                num2len[e]+=1
            else:
                tree.append(e)
                num2len[e]=1
        def dfs(tree_level,cur_sum):
            if tree_level==len(tree):
                return []
            all_res=[]
            #not choose -> +0 choose action
            choice=[0]
            # have 1 2 ,... choose action
            node=tree[tree_level]
            for i in range(1,num2len[node]+1):
                choice.append(node*i)

            for i in range(len(choice)):#i is choose num
                my_choice=choice[i]
                if my_choice+cur_sum==target:
                    all_res.append( i*[node])
                elif my_choice+cur_sum<target:
                    res=dfs(tree_level+1,my_choice+cur_sum)
                    for j in range(len(res)):
                        res[j]=i*[node]+res[j]
                    all_res+=res
                else:
                    pass
            return all_res
        return dfs(0,0)