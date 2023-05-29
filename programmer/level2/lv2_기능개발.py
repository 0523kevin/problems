from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    time = deque([math.ceil((100 - progresses[i])/speeds[i]) for i in range(len(progresses))])
    stack = []
    while time:
        if not stack or stack[0] >= time[0]:
            stack.append(time.popleft())
        else:
            answer.append(len(stack))
            stack.clear()  
    answer.append(len(stack))
    return answer
