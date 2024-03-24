def solution(number, limit, power):
    answer = 0
    def count_nums(a):
        cnt = 0
        for i in range(1, int(a**(1/2))+1):
            if a%i == 0:
                cnt += 1
                if ((i**2) != a) :
                    cnt +=1
            if cnt > limit:
                return power
        return cnt
    for i in range(1, number+1):
        k = count_nums(i)
        if k > limit:
            k = power
        answer += k

    return answer