def solution(m, n, board):
    answer = 0
    board = [list(i) for i in board]
    
    while True:
        remove = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == 0:
                    continue
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    remove.update({(i,j),(i,j+1),(i+1,j),(i+1,j+1)})
        if not remove:
            break
        answer+= len(remove)
        
        for i,j in remove:
            board[i][j] = 0
        
        for j in range(n):
            stack = [board[i][j] for i in range(m) if board[i][j] != 0]
            for i in range(m-1,-1,-1):
                board[i][j] = stack.pop() if stack else 0
        
    return answer
