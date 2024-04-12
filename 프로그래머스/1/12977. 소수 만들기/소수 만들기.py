def solution(nums):
    answer = []
    res=0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                a=nums[i]+nums[j]+nums[k]
                answer.append(a)
    for i in answer:
        
        if all(i%j!=0 for j in range(2,i)):
            res+=1
    return res

    