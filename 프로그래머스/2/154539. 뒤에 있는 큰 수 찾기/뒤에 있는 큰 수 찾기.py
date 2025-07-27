def solution(numbers):
    answer = [-1 for i in range(len(numbers))]
    stack = []
    for idx, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(idx)

            
                
        
    return answer