from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck = deque(truck_weights)
    answer = 0
    sum_bridge = 0
    while bridge:
        answer += 1
        b = bridge.popleft()
        sum_bridge -= b
        if truck:
            if sum_bridge + truck[0] <= weight:
                t = truck.popleft()
                bridge.append(t)
                sum_bridge += t
            else:
                bridge.append(0)
    return answer 
        