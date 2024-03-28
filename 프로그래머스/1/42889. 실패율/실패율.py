def solution(N, stages):
    dic = {}
    user=len(stages)
    for i in range(1,N+1):
        if user!=0:
            dic[i] = stages.count(i)/user
            user-=stages.count(i)
        else:
            dic[i]=0
    
    return sorted(dic,key=lambda x: dic[x],reverse = True)