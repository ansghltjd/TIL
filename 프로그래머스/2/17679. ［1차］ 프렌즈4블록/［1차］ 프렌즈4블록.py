def solution(m, n, board):
    # 문자열 → 리스트로 변환
    board = [list(i) for i in board]
    answer = 0

    while True:
        remove = set()
        # 1. 2x2 같은 블록 탐색
        for i in range(m-1):
            for j in range(n-1):
                block = board[i][j]
                if block == '0':
                    continue
                if block == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    remove.update({(i, j), (i, j+1), (i+1, j), (i+1, j+1)})
        
        # 지울 게 없으면 종료
        if not remove:
            break

        # 2. 블록 제거
        for i,j in remove:
            board[i][j] = '0'
        answer += len(remove)
        
        # 3. 블록 떨어뜨리기 (열 단위 처리)
        for i in range(n):
            stack = [board[j][i] for j in range(m) if board[j][i] != '0']
            for j in range(m-1,-1,-1):
                board[j][i] = stack.pop() if stack else '0'

    return answer