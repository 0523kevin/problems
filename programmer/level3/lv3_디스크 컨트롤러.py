from heapq import heappop, heappush
def solution(jobs):
    answer = 0
    start, now, j = -1, 0, 0
    q = []
    while j < len(jobs):
        for i in jobs:
            if start < i[0] <= now:
                heappush(q, (i[1], i[0]))
        if q:
            curr = heappop(q)
            start = now
            now += curr[0]
            answer += now - curr[1]
            j += 1
        else:
            now += 1
    return answer//len(jobs)