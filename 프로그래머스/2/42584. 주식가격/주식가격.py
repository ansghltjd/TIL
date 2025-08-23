def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for idx,num in enumerate(prices):
        while stack and prices[stack[-1]] > num :
            top = stack.pop()
            answer[top] = idx - top
        stack.append(idx) 
        
    for idx in stack:
        answer[idx] = len(prices)-1 - idx
        
    
    return answer