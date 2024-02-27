def solution(num, total):
    answer = total//num

    num_list=[]
    if num%2==1:
        mid=num//2
        for i in range(answer-mid,answer+mid+1):
            num_list.append(i)
    if num%2==0:
        mid=num//2-1
        for i in range(answer-mid,answer+mid+2):
            num_list.append(i)
    return num_list