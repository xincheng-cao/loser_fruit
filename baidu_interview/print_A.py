'''
0A0
A0A
AAA
A0A
A0A
'''
def print_A(n:int)->list:

    matrix=[
        [' ','A',' '],
        ['A'," ",'A'],
        ['A',"A","A"],
        ['A', " ", 'A'],
        ['A', " ", 'A'],
    ]
    if n==1:
        return matrix
    temp=[]
    for row in range(0,5):
        for col in range(0,3):
            if matrix[row][col]==' ':
                row_len=5**(n-1)
                col_len=3**(n-1)

                temp_temp = []
                for i in range(row_len):
                    temptemp1 = []
                    for j in range(col_len):
                        temptemp1.append(' ')
                    temp_temp.append(temptemp1)

                temp.append(
                    temp_temp
                )
            else:
                temp.append(print_A(n=n-1))
    row_len=5**(n)
    col_len=3**(n)
    #ans_matrix=[[' ']*col_len]*row_len
    ans_matrix=[]
    for i in range(row_len):
        temptemp=[]
        for j in range(col_len):
            temptemp.append(' ')
        ans_matrix.append(temptemp)

    for i in range(len(temp)):
        base_row=i//3
        base_col=i%3

        for row in range(row_len//5):
            for col in range(col_len//3):
                #real_row=base_row*5+row
                real_row=base_row*(5**(n-1))+row
                #real_col=base_col*3+col
                real_col=base_col*(3**(n-1))+col
                ans_matrix[real_row][real_col]=temp[i][row][col]
    return ans_matrix

def pretty_print(temp):
    print()

    for i in range(len(temp)):
        line = ''
        for j in range(len(temp[0])):
            line+=temp[i][j]
        print(line)

def cal_dim(temp):
    print('matrix dim: ',len(temp),len(temp[0]))


for i in range(1,5):
    pretty_print(print_A(i))
    cal_dim(print_A(i))

