def solution(skill, skill_trees):
    answer = []
    cnt = 0
    for i in skill_trees:
        str1 = ''
        for j in i:
            if j in skill:
                str1 += j
        answer.append(str1)
    for i in answer:
        if skill[:len(i)] == i:
            cnt+=1
    return cnt