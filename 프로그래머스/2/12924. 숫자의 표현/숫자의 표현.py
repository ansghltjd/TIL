def solution(n):
    cnt = 0
    for i in range(1,n+1):
        answer = 0
        answer+=i
        if i > n//2:
            cnt+=1
            break
        for j in range(i+1,n):
            answer+=j
            if answer > n:
                break
            if answer==n:
                cnt+=1
                break
    return cnt