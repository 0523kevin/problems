tot = float(input('Enter total price : '))
num = int(input('Number of product : '))
lst = list()
if 1<=tot and tot<=1000000000:
    if 1<=num and num<=100:
        while num>0:
            price, n = map(float, input('price & num : ').split())
            if 1<=price and price<=1000000:
                if 1<=n and n<=10:
                    price_pro = price * n
                    lst.append(price_pro)
                    num -= 1
if sum(lst) != tot:
    print('No')
else:
    print('Yes')
