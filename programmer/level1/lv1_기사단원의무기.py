#정답
def solution(number, limit, power):
    answer = 0
    for num in range(1,number+1):
        weight = getdivisorCnt(num)
        if weight>limit:
            answer += power
        else:
            answer += weight    
    return answer

def getdivisorCnt(num):
    cnt = 0
    if num**0.5 == int(num**0.5):
        cnt -= 1
    for i in range(1, int(num**0.5)+1):
        if num%i == 0:
            cnt += 2 
    return cnt
##########################################

# 약수의 개수 뽑아내기
def getDivisorCnt(num):
    cnt = 0
    if num**0.5 == int(num**0.5):
        cnt -= 1
    for i in range(1, int(num**0.5)+1):
        if num%i == 0:
            cnt += 2
    return cnt

#런타임 7.34 µs ± 203 ns per loop
def getdivisorCnt(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    return cnt


#런타임 1.88 µs ± 13.1 ns per loop
def divisorCnt(num):
    cnt = 0
    if num**0.5 == int(num**0.5):
        cnt -= 1
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            cnt += 2
    return cnt