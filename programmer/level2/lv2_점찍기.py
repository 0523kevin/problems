import math

def mark(k, d):
    if 1<=k and k<=1000000:
        pass
    else:
        print(False)
    if d in range(0,1000000):
        pass
    else:
        print(False)
    lst = list() # 좌표 튜플 형태로 
    for a in range(int(d/k)+1):
        for b in range(int(d/k)+1):
            distance = math.sqrt(pow(a*k,2) + pow(b*k,2))
            if distance <= d:
                lst.append((a*k, b*k))
    return len(lst)

k = int(input('k>>'))
d = int(input('d>>')) 
print(mark(k,d))



# 다른 사람 정답 
def solution(k,d):
    answer = 0
    for i in range(0,d+1, k):
        y = int((d**2-i**2)**(0.5))
        answer += (y//k)+1

