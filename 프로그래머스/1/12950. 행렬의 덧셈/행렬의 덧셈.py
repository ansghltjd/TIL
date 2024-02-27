def solution(arr1, arr2):
    answer=[]
    for i1,j1 in enumerate(arr1) :
        for i2,j2 in enumerate(arr2) :
            if i1 == i2:
                answer.append([j1[n]+j2[n] for n in range(len(j1))])
    return answer