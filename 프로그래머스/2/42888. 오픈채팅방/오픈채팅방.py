def solution(record):
    answer = []
    dic = dict()
    for i in record :
        if 'Enter' in i:
            state, uid, name = i.split()
            dic[uid] = name
        elif 'Change' in i:
            state, uid, name = i.split()
            dic[uid] = name

    for i in record:
        if 'Enter' in i:
            state, uid, name = i.split()
            answer.append(f'{dic[uid]}님이 들어왔습니다.')
        if 'Leave' in i :
            state, uid = i.split()
            answer.append(f'{dic[uid]}님이 나갔습니다.')
    return answer