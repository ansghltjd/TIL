def solution(babbling):
    cnt=0
    for i in babbling:
        temp=i.replace('aya','x').replace('ye','x').replace('woo','x').replace('ma','x')
        if all([i=='x' for i in temp]):
            cnt+=1
    return cnt
        