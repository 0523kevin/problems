# 나의 답
def solution(priorities, location):
    answer = 0
    while True:
        for idx, i in enumerate(priorities):
            maxim = max(priorities)
            if i == maxim:
                answer += 1
                priorities[idx] = 0
                if idx == location:
                    return answer
