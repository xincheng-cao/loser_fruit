class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        res=[]
        for ss in range(len(strs)):
            flag=True
            for jj in range(len(strs)):
                if ss==jj: continue
                s=strs[ss]
                j=strs[jj]

                s_idx=0
                j_idx=0

                while j_idx<len(j) and s_idx<len(s):
                    if s[s_idx]==j[j_idx]:
                        s_idx+=1
                        j_idx+=1
                    else:
                        j_idx+=1
                if s_idx==len(s):
                    flag=False
                    break
            if flag:
                res.append(s)
        max_len=-1
        for r in res:
            if len(r)>max_len:max_len=len(r)
        return max_len