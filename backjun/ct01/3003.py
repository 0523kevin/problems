cnum = list(map(int, input().split()))
piece = [1,1,2,2,2,8]

lst = []
for i in range(len(piece)):
    res = piece[i] - cnum[i]
    lst.append(res)
print(*lst)
