M = int(input())
N = int(input())
answer=[]
for i in range(M,N+1):
    if i>1:
        for j in range(2,i+1):
            if j==i:
                answer.append(i)
            if i%j==0:
                break
if len(answer)>0:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)