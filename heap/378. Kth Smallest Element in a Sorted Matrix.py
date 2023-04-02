import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        li=[]
        for row in range(len(matrix)):
            li.append(
                (
                    matrix[row][0],
                    row,
                    0
                )
            )
        # heapq.heapify(li)
        for i in range(k):
            #print(li)
            ans,row,col=heapq.heappop(li)

            if i==k-1:break

            if col+1<len(matrix[0]):
                heapq.heappush(li,
                (matrix[row][col+1],row,col+1)
                )
            else:
                pass
                # not going to push the one below bc it will
                # introduce dup in li
        return ans









