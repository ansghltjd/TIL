def solution(ingredient):
    answer = []
    cnt=0
    for i in ingredient:
        answer.append(i)
        if answer[-4:] == [1,2,3,1]:
            del answer[-4:]
            cnt+=1
    return cnt
    