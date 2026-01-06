#에라토스테네스체에 대해서 확인해볼 필요가 있다 소수 알고리즘에 중요함
import math
def solution(n):
    answer = 0
    lst=[True for i in range(n+1)]
    
    for i in range(2,int(math.sqrt(n))+1):
        if lst[i]==True:
            j=2
            while i*j<=n:
                lst[i*j]=False
                j+=1
    for i in range(2,n+1):
        if lst[i]:
            answer+=1
    return answer