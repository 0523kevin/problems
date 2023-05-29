# 내 답
from collections import Counter
def solution(X, Y):
    answer = ''
    x_num = Counter(list(X))
    y_num = Counter(list(Y))
    ggung = {}
    for i in X:
        if i in Y:
            if x_num[i] >= y_num[i]:
                ggung[i] = y_num[i]
            else:
                ggung[i] = x_num[i]
    sort = sorted(ggung.items(), key = lambda t:t[0],reverse = True)
    
    if len(sort)<1:
        answer = '-1'
    else:
        if sort[0][0] == '0':
            answer = '0'
        else:
            for i in sort:
                answer += i[0]*i[1]
    return answer



# 간단한 방법
def solution(X,Y):
    answer = ''
    for i in range(9,-1,-1):
        answer += (str(i)*min(X.count(str(i)), Y.count(str(i))))
    if answer == '':
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else:
        return answer
    return answer