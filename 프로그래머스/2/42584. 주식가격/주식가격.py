def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for idx, num in enumerate(prices):
        while stack and prices[stack[-1]] > prices[idx]:
            top = stack.pop()
            answer[top] = idx - top
        stack.append(idx)
    for i in stack:
        answer[i] = len(prices)-1 - i
    return answer