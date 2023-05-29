from heapq import heapify, heappop, heappush
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while scoville:
        a1 = heappop(scoville)
        if a1 >= K:
            break
        if len(scoville) == 0:
            return -1
        a2 = heappop(scoville)
        new = a1 + 2* a2
        heappush(scoville, new)
        answer += 1
    return answer