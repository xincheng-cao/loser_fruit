class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top=0
        bottom=len(matrix)-1

        while top < bottom:
            matrix[top],matrix[bottom]=\
            matrix[bottom],matrix[top]

            top+=1
            bottom-=1
        #print(matrix)
        for row in range(len(matrix)):
            for col in range(row,len(matrix[0])):
                matrix[row][col],matrix[col][row]=\
                matrix[col][row],matrix[row][col]



