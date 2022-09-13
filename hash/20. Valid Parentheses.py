class Solution:
    def isValid(self, s: str) -> bool:
        if s.__len__()%2==1:
            return False
        stack=[]
        left={'(':0,'[':1,'{':2}
        right={'}':2,']':1,')':0}
        for char in s:
            if len(stack)==0:
                if char in left:
                    stack.append(char)
                else:
                    return False
            else:
                if char in left:
                    stack.append(char)
                else:
                    temp_char=stack.pop()
                    if temp_char in left:
                        if left[temp_char]==right[char]:
                            continue
                        else:
                            return False
                    else:
                        return False
        if stack.__len__()==0:
            return True
        else:
            return False
