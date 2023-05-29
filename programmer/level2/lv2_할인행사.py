# 정답 
from collections import Counter
def solution(want, number, discount):
    answer = 0
    want_num = dict(zip(want, number))
    for i in range(len(discount)-9):
        if Counter(discount[i:i+10]) == want_num:
            answer += 1

    return answer