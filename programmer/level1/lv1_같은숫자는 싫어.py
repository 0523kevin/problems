from collections import deque
def solution(arr):
    answer = []
    # 런타임 에러 방지를 위해 queue 구조를 deque 자료구조로 구현
    arr = deque(arr)
    while arr:
        n = arr.popleft()
        if not answer:
            answer.append(n)
        if answer[-1] != n:
            answer.append(n)
    return answer
