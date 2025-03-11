def solution(want, number, discount):
    answer = 0
    want_dic = {i:j for i,j in zip(want,number)}
    
    for i in range(len(discount)-9):
        discount_a = discount[i:i+10]
        discount_dic = {i:discount_a.count(i) for i in want}
        if want_dic == discount_dic:
            answer+=1
    return answer