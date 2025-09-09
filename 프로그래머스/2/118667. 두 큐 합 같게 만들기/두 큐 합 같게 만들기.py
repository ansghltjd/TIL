from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    target = (sum1 + sum2) // 2
    
    if (sum1+sum2) % 2 == 1:
        return -1
    
    answer = 0
    max_cnt = len(q1)*3
    
    while answer < max_cnt:
        if sum1 == target and sum2 == target:
            return answer
        elif sum1 < target:
            if not q2:
                return -1
            num = q2.popleft()
            q1.append(num)
            sum1 += num
            sum2 -= num
        else:
            if not q1:
                return -1
            num = q1.popleft()
            q2.append(num)
            sum1 -= num
            sum2 += num
        answer += 1
    return -1