class Solution:
    KEY = {'2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits)==0:
            return []
        if len(digits)==1:
            return self.KEY[digits[0]]
        front=self.letterCombinations(digits[:-1])
        front_len=len(front)
        cur_char=digits[-1]
        front=front*len(self.KEY[cur_char])
        cur=[]
        for i in range(len(self.KEY[cur_char])):
            cur+=[self.KEY[cur_char][i]]*front_len
        for i in range(len(front)):
            front[i]+=cur[i]
        return front