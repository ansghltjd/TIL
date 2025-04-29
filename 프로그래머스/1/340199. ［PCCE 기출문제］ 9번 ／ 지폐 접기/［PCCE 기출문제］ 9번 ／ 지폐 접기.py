def solution(wallet, bill):
    answer = 0

    while max(wallet) < max(bill) or min(wallet) < min(bill):
        answer+=1
        bill[bill.index(max(bill))] = max(bill) // 2
            
    return answer