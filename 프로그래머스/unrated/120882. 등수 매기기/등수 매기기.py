def solution(score):
    
    answer = [sum(i)/2 for i in score]
    
    sorted_answer=sorted(answer,reverse=True)
    
    rank=[sorted_answer.index(i)+1 for i in answer]
    return rank