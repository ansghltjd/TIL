def solution(id_list, report, k):
    answer = []

    users = {user:set() for user in id_list}
    users_cnt = {user:0 for user in id_list}


    for s in report:
        a, b = s.split(" ")
        users[b].add(a)

    for user, reported_users in users.items():
        if len(reported_users) >= k:
            for reported_user in reported_users:
                users_cnt[reported_user] += 1

    answer = [users_cnt[user] for user in users_cnt]    

    return answer 