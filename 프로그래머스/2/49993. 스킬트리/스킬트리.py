def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        a = ''.join([j for j in i if j in skill])
        if skill[:len(a)] == a:
            answer+=1
    return answer