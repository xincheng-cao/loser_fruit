class Solution:
    def fry(self,arr,pos):
        left=arr[:pos+1]
        right=arr[pos+1:]
        left.reverse()
        return left+right

    def pancakeSort(self, arr: List[int]) -> List[int]:
        cur_max_e=len(arr)
        res=[]
        while cur_max_e>1:
            e_pos=arr.index(cur_max_e)
            arr=self.fry(arr,e_pos)
            res.append(e_pos+1)
            arr=self.fry(arr,cur_max_e-1)
            res.append(cur_max_e)
            cur_max_e-=1
        return res