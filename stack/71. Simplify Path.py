class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        li=path.split('/')
        for e in li:
            if e.__len__()==0:
                continue
            if e=='..':
                if stack.__len__()>=1:
                    stack.pop()
                continue
            if e=='.':
                continue
            stack.append(e)
        return '/'+'/'.join(stack)