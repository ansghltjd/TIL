def solution(record):
    answer = []
    uid_name = {}
    actions = []
    
    for r in record:
        li = r.split()
        state, uid = li[0], li[1]
        
        if state in ('Enter', 'Change'):
            uid_name[uid] = li[2]
        if state in ('Enter','Leave'):
            actions.append((uid,state))
    
    for i in actions:
        uid, state = i[0], i[1]
        
        if state == 'Enter':
            answer.append(f'{uid_name[uid]}님이 들어왔습니다.')
        else:
            answer.append(f'{uid_name[uid]}님이 나갔습니다.')
        
        
    return answer