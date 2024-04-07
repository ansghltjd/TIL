def solution(board, h, w):
    answer = board[h][w]
    cnt=0
    mov=[[-1,0],[1,0],[0,-1],[0,1]]
    for i,j in mov:
        try :
            if h+i == -1 or w+j == -1:
                continue
            if board[h+i][w+j] == answer:
                cnt+=1
        except :
            continue
    return cnt