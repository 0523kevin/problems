#Answer
from math import gcd
from functools import reduce
def solution(arrayA, arrayB):
    answer = 0
    arrayA.sort()
    arrayB.sort()
    gcda, gcdb = reduce(gcd, arrayA), reduce(gcd, arrayB)
    if all(i % gcdb != 0 for i in arrayA):
        answer.append(gcdb)
    if all(i % gcda != 0 for i in arrayB):
        answer.append(gcda)
    return max(answer) if answer else 0 



from functools import reduce
from math import gcd
def solution(arrayA, arrayB):
    answer = []
    a1 = reduce(gcd, arrayA)
    b1 = reduce(gcd, arrayB)

    if all(i % b1 for i in arrayB):
        answer.append(b1)
    if all(i % a1 for i in arrayA):
        answer.append(a1)
    
    return max(answer) if answer else 0
    
