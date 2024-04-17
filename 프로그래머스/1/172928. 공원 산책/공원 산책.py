def solution(park, routes):
    n=len(routes)

    dic={'W':0,'S':1,'E':2,'N':3}
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j]=='S':
                a,b=i,j #a=y , b=x

    for i in routes:
        di = i[0]
        le = int(i[2])
        ty,tx = a,b
        for j in range(le):
            t1=a+dy[dic[di]]
            t2=b+dx[dic[di]]
            if t1>=0 and t2>=0 and t1<len(park) and t2<len(park[0]) and park[t1][t2]!='X':
                a,b=t1,t2
            else:
                a,b = ty,tx
                break
    answer=[a,b]

    return answer