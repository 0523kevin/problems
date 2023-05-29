count, lst = int(input('')), list()
while count>0:
    a, b = map(int, input('').split())
    sum = a + b
    lst.append(sum)
    count = count-1

for i in lst:
    print(i)
