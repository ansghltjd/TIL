from collections import defaultdict
import math
def solution(fees, records):
    basic_time, basic_fee, unit_time, unit_fee = fees
    
    parking = dict()
    total = defaultdict(int)
    
    def time_to_min(time_str):
        hour, minute = map(int,time_str.split(':'))
        return hour * 60 + minute
    
    for record in records:
        time_str, car_num, state = record.split()
        time = time_to_min(time_str)
        if state == 'IN':
            parking[car_num] = time
        if state == 'OUT':
            in_time = parking.pop(car_num)
            total[car_num] += time - in_time
    
    answer = []
    for car_num, time in parking.items():
        total[car_num] += time_to_min('23:59') - time
        
    for car_num in sorted(total.keys()):
        time = total[car_num]
        if time > basic_time:
            answer.append(basic_fee + math.ceil((time - basic_time) / unit_time) * unit_fee)
        else:
            answer.append(basic_fee)
        
        
    return answer