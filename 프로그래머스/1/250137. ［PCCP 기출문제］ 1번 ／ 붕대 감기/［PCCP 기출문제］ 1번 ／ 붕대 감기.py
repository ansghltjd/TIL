def solution(bandage, health, attacks):
    answer = 0
    band_time = 0
    hp = health
    attack_time={i[0]:i[1] for i in attacks}
    for i in range(1,attacks[-1][0]+1):
            if i in attack_time:
                hp -= attack_time[i]
                band_time=0
                if hp<=0:
                    return -1
            else:
                band_time+=1
                hp+=bandage[1]
                if (band_time % bandage[0]) ==0:
                    hp+=bandage[2]
            if hp>health:
                hp=health
            
            
    return hp