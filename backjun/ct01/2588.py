fnum = int(input())
snum = int(input())

lst = []
for i in str(snum):
    lst.append(i)

for i in range(len(lst)):

    print(fnum*int(lst[-1-i]))
print(fnum*snum)
