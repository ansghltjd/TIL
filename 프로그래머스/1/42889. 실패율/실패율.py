def solution(N, stages):
    answer = [0 for i in range(N)]
    sta = [i for i in range(1,N+1)]
    user=len(stages)
    for i in range(1,N+1):
        answer[i-1] = stages.count(i)/user
        user-=stages.count(i)
        if user == 0 :
            break
    zipped= sorted(zip(sta,answer),reverse=True,key = lambda x : x[1])
    
    return [i[0] for i in zipped]