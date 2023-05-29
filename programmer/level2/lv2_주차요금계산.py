import math
def solution(fees, records):
    answer = []
    basic_min = fees[0]
    basic_won = fees[1]
    unit_min = fees[2]
    unit_won = fees[3]

    cars = set([i[1] for i in records.split()])
    time_list = {k : 0 for k in cars}
    check = {}

    for record in records.split():
        if record[1] not in check:
            check[record[1]] = record[0]
        else:
            time = check.pop(record[1])
            time_list[record[1]] += (record[0].split(':')[0] - time.split(':')[0]) *60 + record[0].split(':')[1] - time.split(':')[1]

    if check:
        for car in check.keys():
            time_list[car] += (23 - check[car].split(':')[0]) * 60 + 59 - check[car].split(':')[1]

    
    for min_time in sorted(time_list.items(), key = lambda x:x[0]).values():
        if min_time > basic_min:
            tot = basic_won + math.ceil((min_time - basic_min)/unit_min) * unit_won
            answer.append(tot)
        else:
            answer.append(basic_won)
    
    return answer



# out time, in time 나눠서 저장하여 가독성 높임
import math
def solution(fees, records):
    basic_min = fees[0]
    basic_fee = fees[1]
    minute = fees[2]
    cost = fees[3]
    records_sep = [i.split() for i in records]
    car = set([i[1] for i in records_sep])
        
    tot_fee = {k: 0 for k in car}
    check = {}
    for record in records_sep:
        if record[1] not in check.keys():
            check[record[1]] = record[0]
        elif record[-1] == 'OUT':
            out_time = int(record[0].split(':')[0]) * 60 + int(record[0].split(':')[1])
            in_time = int(check[record[1]].split(':')[0]) * 60 + int(check[record[1]].split(':')[1]) 
            tot_fee[record[1]] += out_time - in_time
            del check[record[1]]
    if check:
        for i in check.items():
            out_time = 1439
            in_time = int(i[1].split(':')[0]) * 60 + int(i[1].split(':')[1])
            tot_fee[i[0]] += out_time - in_time
    
    result = []
    for k, v in tot_fee.items():
        if v <= basic_min:
            result.append((k, basic_fee))
        else:
            ans = (k, basic_fee + cost * math.ceil((v-basic_min)/minute))
            result.append(ans)
    return list(map(lambda x:x[1], sorted(result)))
    
            
    