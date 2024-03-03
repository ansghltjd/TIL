def solution(t, p):
    answer=0
    cnt=0
    for i in range(len(p),len(t)+1):
        if int(t[cnt:i])<=int(p):
            answer+=1
        cnt+=1
    return answer
    