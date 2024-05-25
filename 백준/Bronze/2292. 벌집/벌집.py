num=int(input())
numbox=1
cnt=1

while num > numbox :
    numbox += cnt*6
    cnt+=1
print(cnt)