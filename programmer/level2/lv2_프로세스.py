def solution(priorities, location):
    answer = 0
    while True:
        for i, p in enumerate(priorities):
            maximum = max(priorities)
            if p == maximum:
                priorities[i] = 0
                answer += 1
                if i == location:
                    return answer