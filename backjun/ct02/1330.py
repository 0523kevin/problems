a, b = map(int, input('Enter Two numbers: ').split())

#제한 조건에 따른 반환 값
if a>=-1000 and b<=10000:
    if a>b:
        print('>')
    elif a<b:
        print('<')
    elif a==b:
        print('==')
elif a<-10000 and b<=10000: print('first number should be bigger than -10000 or same')
elif a>=-10000 and b>10000: print('second number should be smaller than 10000 or same')
else: print('first number should be bigger than -10000 or same\n','&\n','second number should be smaller than 10000 or same')
