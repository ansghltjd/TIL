def solution(answers):
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    answer = [0,0,0]
    for i,j in enumerate(answers) :
        if j == a1[i%5]:
            answer[0]+=1
        if j == a2[i%8]:
            answer[1]+=1
        if j == a3[i%10]:
            answer[2]+=1
    res=[]
    for i,j in enumerate(answer):
        if j == max(answer):
            res.append(i+1)
    return res
            