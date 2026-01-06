#문제에 대해 확실히 이해했지만 연산 순서 잘못 입력함
def solution(a, b, n):
    answer = 0
    remain=0
    while n>=a:
        if n%a==0:
            remain=n%a
            n=(n//a)*b
            answer+=n
            n+=remain
            
        elif n%a!=0:
            remain=n%a
            n=(n//a)*b
            answer+=n
            n+=remain
    
    return answer