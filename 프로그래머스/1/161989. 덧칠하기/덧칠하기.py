def solution(n, m, section):
    wall = [1 for i in range(n)]
    for i in section :
        wall[i-1]=0
    idx=section[0]-1
    cnt=0
    while idx<n:
        if wall[idx] == 0:
            idx+=m
            cnt+=1
        else:
            idx+=1
    return cnt