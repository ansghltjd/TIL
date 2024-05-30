a,b=map(int,input().split())
num = [i for i in range(1,a+1) if a%i==0]
try:
    print(num[b-1])
except:
    print(0)