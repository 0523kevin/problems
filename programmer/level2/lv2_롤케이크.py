from collections import Counter
def solution(topping):
    answer = 0
    dic = Counter(topping)
    box = set()
    for i in topping:
        dic[i] -= 1
        box.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(box):
            answer += 1
    return answer

solution([1,2,1,3,1,4,1,2])


# def solution(topping):
#     answer = 0
#     for n in range(len(topping)):
#         a = set(topping[:n])
#         b = set(topping[n:])
#         if len(a) == len(b):
#             answer+=1
#     return answer

# 런타임 너무 긺
from collections import deque, Counter
def solution(topping):
    box = set()
    cnt = Counter(topping)
    dq = deque(topping)
    answer = 0 
    for i in range(len(dq)):
        n = dq.popleft()
        box.add(n)
        if len(box) == len(set(dq)):
            answer += 1
    return answer
        



