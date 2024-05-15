N = int(input())

m = [[0]*100 for i in range(100)]

for _ in range(N):
     x,y = map(int,input().split())
     for i in range(x,x+10):
        for j in range(y,y+10):
            m[i][j]=1
answer=0
for i in range(100):
    answer+=m[i].count(1)
print(answer)