def solution(numbers):
    answer = []
    for i,j in enumerate(numbers[:-1]) :
        for k in numbers[i+1:]:
            answer.append(k+j)
    answer=set(answer)
    return sorted(answer)