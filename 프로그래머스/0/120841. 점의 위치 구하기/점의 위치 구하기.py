def solution(dots):
    answer = 0
    
    if dots[0]>0 and dots[1]>0:
        return 1
    elif dots[0]<0 and dots[1]>0:
        return 2
    elif dots[0]<0 and dots[1]<0:
        return 3
    elif dots[0]>0 and dots[1]<0:
        return 4
    