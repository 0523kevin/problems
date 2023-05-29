#구구단
num = int(input(''))
if num>=1 and num<=9:
    for i in range(9):
        print(num, '*', i, ' = ', num*i)
