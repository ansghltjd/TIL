def solution(n, lost, reserve):
    answer = [0 for i in range(n+1)]
    lost_=set(lost)
    reserve_=set(reserve)
    lost = lost_ - reserve_
    reserve = reserve_ - lost_
    c=0
    for i in lost :
        answer[i]=1
        c+=1
    for i in reserve :
        if i>1 and answer[i-1] ==1:
            answer[i-1]=0
            c-=1
            continue
        if i<n and answer[i+1] ==1:
            answer[i+1]=0
            c-=1
    return n-c