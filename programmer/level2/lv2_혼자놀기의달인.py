import random
def solution(cards):
    boxes = dict(enumerate(cards, start=1))
    group = []
    while boxes:
        visit = set()
        box_num = random.choice(list(boxes.keys()))
        while box_num not in visit:
            visit.add(box_num)
            cardnum = boxes.pop(box_num)
            # print(boxes)
            box_num = cardnum
        group.append(len(visit))
    group.sort(reverse = True)
    return group[0] * group[1] if len(group)>1 else 0    