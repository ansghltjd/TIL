def solution(people, limit):
    people.sort(reverse=True)
    answer=0
    first=0
    last=len(people)-1
    while first<=last:
        if people[first] + people[last] <= limit:
            last-=1
        first+=1
        answer+=1
    return answer