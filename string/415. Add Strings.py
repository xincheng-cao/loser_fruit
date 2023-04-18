class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        max_len=max(len(num1),len(num2))
        adv=0
        res=''
        num1='0'*(max_len-len(num1))+num1
        num2='0'*(max_len-len(num2))+num2
        for i in range(max_len-1,-1,-1):
            temp_res=int(num2[i])+int(num1[i])+adv
            res=str(temp_res%10)+res
            adv=temp_res//10
        if adv !=0:
            res=str(adv)+res
        return res