from collections import defaultdict
import math
def solution(fees, records):
    parking = dict()
    total_time = defaultdict(int)
    basic_time, basic_fee, unit_time, unit_fee = fees
    
    def hour_to_minute(str_time):
        hour, minute = map(int,str_time.split(':'))
        return hour * 60 + minute
    
    for record in records:
        str_time, car_num, state = record.split()
        time = hour_to_minute(str_time)
        if state == 'IN':
            parking[car_num] = time 
        elif state == 'OUT':
            in_time = parking.pop(car_num)
            total_time[car_num] += time - in_time
            
    answer = []
    
    for car_num, in_time in parking.items():
        total_time[car_num] += hour_to_minute('23:59') - in_time
    
    for car_num in sorted(total_time.keys()):
        time = total_time[car_num]
        if time <= basic_time:
            answer.append(basic_fee)
        else:
            answer.append(basic_fee + math.ceil((time-basic_time) / unit_time ) * unit_fee)
    return answer