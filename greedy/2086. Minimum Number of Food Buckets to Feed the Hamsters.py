class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        hamsters=list(hamsters)
        if len(hamsters) == 1:
            if hamsters[0] == 'H':
                return -1
            else:
                return 0
        if len(hamsters) == 2:
            if hamsters[0] == 'H' and hamsters[1] == 'H': return -1
            if hamsters[0] == 'H' or hamsters[1] == 'H': return 1
            return 0
        res = 0
        i = 0
        while i < len(hamsters):
            if hamsters[i] == 'H':
                if i == 0 and hamsters[1] == 'H':
                    return -1
                elif i==0:
                    res += 1
                    hamsters[i+1]='F'
                    i += 3
                    #if i-1<len(hamsters): hamsters[i - 1] = '.'
                    continue
                if i == len(hamsters) - 1 and hamsters[i - 1] == 'H':
                    return -1
                elif i==len(hamsters) - 1 :
                    res += 1
                    #hamsters[i+1]='F'
                    i += 3
                    #if i-1<len(hamsters): hamsters[i - 1] = '.'
                    continue

                if hamsters[i - 1] == 'H' and hamsters[i + 1] == 'H': return -1
                if hamsters[i - 1] == 'H':
                    if hamsters[i-2]=='F':
                        hamsters[i+1]='F'
                        res+=1
                    else:
                        hamsters[i+1]='F'
                        hamsters[i-2]='F'
                        res+=2
                    i += 3
                    #if i-1<len(hamsters): hamsters[i - 1] = '.'
                else:
                    if hamsters[i + 1] == '.':
                        res += 1
                        hamsters[i+1]='F'
                        i += 3
                        #if i-1<len(hamsters): hamsters[i - 1] = '.'
                    else:
                        i += 1
            else:
                i += 1
        return res
