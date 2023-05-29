from heapq import heappush, heappop
def solution(operations):
    max_heap, min_heap = [], []
    for op in operations:
        if op == 'D 1':
            if max_heap:
                heappop(max_heap)
                if not max_heap or -max_heap[0] < min_heap[0]:
                    min_heap, max_heap = [], []
        elif op == 'D -1':
            if min_heap:
                heappop(min_heap)
                if not min_heap or -max_heap[0] < min_heap[0]:
                    min_heap, max_heap = [], []
        else:
            heappush(max_heap, -int(op[2:]))
            heappush(min_heap, int(op[2:]))
    if not min_heap:
        return [0, 0]
    return [-heappop(max_heap), heappop(min_heap)]
                    