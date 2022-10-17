class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_res=x^y
        res=0
        while xor_res!=0:
            if xor_res&1==1:
                res+=1
            xor_res=xor_res>>1
        return res