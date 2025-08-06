def solution(skill, skill_trees):
    answer = 0
    
    for i in skill_trees:
        s = ''.join([j for j in i if j in skill])
        if skill[:len(s)] == s:
            answer+=1
    return answer