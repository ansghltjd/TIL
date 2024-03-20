def solution(cards1, cards2, goal):
    answer = []
    li,ri = 0 , 0
    for g in goal:
        if li < len(cards1) and g == cards1[li]:
            li+=1
        elif ri < len(cards2) and g == cards2[ri]:
            ri+=1
    if li+ri == len(goal):
        return 'Yes'
    else:
        return 'No'
            