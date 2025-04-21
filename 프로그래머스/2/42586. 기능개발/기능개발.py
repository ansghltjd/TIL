def solution(progresses, speeds):
    answer = []
    a = []
    count = 1
    for idx, i in enumerate(progresses):
        i = 100-i
        if i % speeds[idx]==0:
            a.append(i//speeds[idx])
        else:
            a.append(i//speeds[idx]+1)
    f = a[0]
    for day in a[1:]:
        if day <= f:
            count+=1
        else:
            answer.append(count)
            count=1
            f = day
    answer.append(count)
    return answer