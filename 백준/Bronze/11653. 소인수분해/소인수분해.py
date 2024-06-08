num = int(input())
a = 2
if num!=1:
    while 1:
        if num%a==0:
            print(a)
            num=num//a
        else:
            a+=1
        if num==1:
            break
            