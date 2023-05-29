from collections import deque
def solution(arr):
    answer = []
    arr_dq = deque(arr)
    for i in range(len(arr)):
        n = arr_dq.popleft()
        if answer == []:
            answer.append(n)
        if n != answer[-1]:
            answer.append(n)
    return answer