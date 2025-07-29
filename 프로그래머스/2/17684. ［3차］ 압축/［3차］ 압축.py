def solution(msg):
    answer = []
    lst = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    max_len, move_len = 1, 1
    while msg:
        if msg[0:move_len] in lst:
            answer.append(lst.index(msg[:move_len])+1)
            lst.append(msg[:move_len+1])
            msg = msg[move_len:]
            max_len = (move_len+1) if move_len+1 > max_len else max_len
            move_len = max_len
        else : 
            move_len -= 1
    return answer