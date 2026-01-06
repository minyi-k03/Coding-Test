import math
def solution(balls, share):
    answer = 0
    balls_factorial=math.factorial(balls)
    share_factorial=math.factorial(share)
    sub_factorial=math.factorial(balls-share)
    
    answer=balls_factorial//(sub_factorial*share_factorial)
    
    return answer