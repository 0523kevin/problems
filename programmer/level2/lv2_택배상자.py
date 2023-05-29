# 정답
def solution(order):
    order.reverse()
    belt = list(range(len(order), 0, -1))
    sub = []
    truck = 0
    while True:
        if belt and order and order[-1] == belt[-1]:
            belt.pop()
            order.pop()
            truck += 1
        elif sub and order and order[-1] == sub[-1]:
            sub.pop()
            order.pop()
            truck += 1
        elif belt:
            sub.append(belt.pop())
        else:
            break
    return truck