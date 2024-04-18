def solution(players, callings):
    answer = {j:i for i,j in enumerate(players)}
    for i in callings:
        rank = answer[i]
        
        answer[i]-=1
        answer[players[rank-1]]+=1
        
        players[rank],players[rank-1] = players[rank-1],i
    return players