import pprint

def solve(bo):
    '''
    回溯方法找答案
    '''

    empty = find_empty(board)
    if not empty:
        return True  # 如果没有未填充的位置，数独已解决
    row, col = empty

    # 尝试填充数字1到9
    for num in range(1, 10):
        if valid(board, row, col,num, ):
            board[row][col] = num  # 填充数字
            if solve(board):
                return True  # 递归求解数独
            board[row][col] = 0  # 如果无法解决，回溯

    return False  # 数独无解




def valid(bo,row,col,num):
    for i in range(0,len(bo)):
        if  (bo[row][i]==num and col!=i) or(bo[i][col]==num and row!=i):
            return False
    
    box_x=col//3
    box_y=row//3


    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if bo[i][j]==num and (i!=row or j!=col):
                return False
    return True






def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if board[i][j] == 0:
                return (i,j)
    return None




def print_board(bo):
    for i in range(len(bo)):
        if i%3==0 and i!=0:
            print('-------------------')
        for j in range(len(bo[0])):
            if j %3==0:
                print(' | ',end='')
            if j==8:
                print(bo[i][j],end='\n')
            else:
                print(str(bo[i][j]+' ',end=''))

board=[[7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]]


pp=pprint.PrettyPrinter(width=41,compact=True)
solve(board)
pp.pprint(board)