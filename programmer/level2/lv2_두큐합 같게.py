# 정답
from collections import deque
def solution(queue1, queue2):
    answer = -2
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    tot = sorted(deque(queue1 + queue2))
    max = tot.pop()
    if max > sum(tot):
        answer += 1
    else:
        answer += 2
        while True:
            if sum(dq1) == sum(dq2):
                break
            elif sum(dq1) > sum(dq2):
                temp = dq1.popleft()
                dq2.append(temp)
                answer += 1
            else:
                temp = dq2.popleft()
                dq1.append(temp)
                answer += 1
    return answer