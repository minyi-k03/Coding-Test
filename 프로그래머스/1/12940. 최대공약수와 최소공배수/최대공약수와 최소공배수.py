#해당 파이썬 버전이 3.8.5라 math모듈에 lcm 모듈 사용 불가능 
import math
def solution(n, m):
    answer=[]
    result=math.gcd(n,m)
    result2=(n*m)//math.gcd(n,m)
    answer.append(result)
    answer.append(result2)
    
    
    return answer