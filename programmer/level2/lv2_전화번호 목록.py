def solution(phone_book):
    answer = True
    phone_book.sort()
    phones = dict(enumerate(phone_book))
    for i in range(len(phone_book)-1):
        if phones[i+1].startswith(phones[i]):
            answer = False
            break  
    return answer