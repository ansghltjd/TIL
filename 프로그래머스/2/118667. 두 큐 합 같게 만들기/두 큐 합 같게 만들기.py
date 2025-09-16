from collections import deque
def solution(queue1, queue2):
    q1, sum1 = deque(queue1), sum(queue1)
    q2, sum2 = deque(queue2), sum(queue2)
    
    if (sum1+sum2) % 2 == 1:
        return -1
    
    target = (sum1+sum2) // 2
    max_cnt = len(q1) * 3
    answer = 0
    while max_cnt > answer :
        if sum1 == target:
            return answer
        elif sum1 > sum2:
            num = q1.popleft()
            q2.append(num)
            sum1 -= num
            sum2 += num
        else:
            num = q2.popleft()
            q1.append(num)
            sum2 -= num
            sum1 += num
        answer+=1
    
    
    return -1