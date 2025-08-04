def solution(order):
    answer = []
    stack = []
    o_n=0
    s_n=1
    for i in range(len(order)+1):
        while stack and order[o_n] == stack[-1]  :
            o_n+=1
            answer.append(stack.pop())
        stack.append(s_n)
        s_n+=1
    return len(answer)