class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(level:int,labelled_str:str):
            #100.200.222.22
            if level==3:
                temp=labelled_str.split('.')
                if temp[-1]=='':
                    return []
                if temp[-1][0]=='0' and len(temp[-1])>1:
                    return []
                if int(temp[-1])>255:
                    return []
                return [labelled_str]
            temp=labelled_str.split('.')
            if temp[-1].startswith('0'):
                last=temp.pop()
                temp.append(last[:1])
                temp.append(last[1:])
                res=dfs(level+1,'.'.join(temp))
                new_res=[]
                for e in res:
                    new_res.append(e)
                return new_res
            else:
                new_res=[]
                last=temp.pop()
                if last=='':
                    return new_res
                for ii in range(1,4):
                    left=last[:ii]
                    right=last[ii:]
                    if int(left)>255:
                        break
                    temp.append(left)
                    temp.append(right)
                    res=dfs(level+1,'.'.join(temp))
                    for e in res:
                        new_res.append(e)
                    temp.pop()
                    temp.pop()

                return new_res
        return dfs(0,s)
