a = []
x,y= 0,0
max_a=0
for i in range(9):
    a.append(list(map(int,input().split())))
    if max(a[i]) >= max_a:
        max_a=max(a[i])
        x,y = i+1,a[i].index(max_a)+1
print(max_a)
print(x,y)