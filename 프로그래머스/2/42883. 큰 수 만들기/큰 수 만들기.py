def solution(number, k):
    stack = []
    to_remove = k
    
    for digit in number:
        while stack and to_remove > 0 and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)
    
    # 슬라이싱으로 남은 제거 처리
    result = ''.join(stack[:len(stack) - to_remove])
    return result

