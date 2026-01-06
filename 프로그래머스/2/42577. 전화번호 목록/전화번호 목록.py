def solution(phone_book): #phone_book리스트의 0번 인덱스 값을 고정적으로 부여해서 틀림
    answer = True          #반복문을 이용하여 phone_book의 요소들을 모두 검사했어야 했음
    phone_book.sort()
    
    for p1,p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
        
        
    return True
    
    
    
    