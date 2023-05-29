# 정답
def dot_value(k):
    y = [k] #미리 첫 k 값을 포함시켜놓았다.
    while k != 1:
        if k%2 == 0:
            k /= 2
        else:
            k = k*3 + 1
        y.append(k)
    return y

def solution(k, ranges):
    answer = list()
    y = dot_value(k)
    for a,b in ranges:
        c = len(y)+b
        if a >= c:   # 범위산정 제일 중요, a 와 b 의 인덱스가 서로 크로스 오버 되지 않게
            answer.append(-1)
        else:
            area = 0
            for i in range(a,c-1):
                area += 0.5*(y[i]+y[i+1])
            answer.append(area)
    return answer

        
