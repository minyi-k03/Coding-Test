def solution(n):
    answer = 0
    fibo=[0,1] #미리 배열에 저장해서 중복되는 연산을 줄인다(D.P)
    
    for i in range(2,n+1):
        fibo.append(fibo[i-1]+fibo[i-2])
    
    answer=fibo[-1]%1234567
    return answer