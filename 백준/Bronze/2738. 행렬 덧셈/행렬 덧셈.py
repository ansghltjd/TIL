
a,b=[],[]
n,m = map(int,input().split())
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    b.append(list(map(int,input().split())))
for row in range(n):
    for col in range(m):
        print(a[row][col] + b[row][col], end=' ')
    print()
