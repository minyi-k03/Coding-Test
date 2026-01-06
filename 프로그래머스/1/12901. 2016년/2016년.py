def solution(a, b):
    answer = ''
    tmp = 0
    week = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    
    month_day = ["0","31","29","31","30","31","30","31","31","30","31","30"]
    
    for i in range(0,a):
        tmp+=int(month_day[i])
        answer = week[(tmp+b-1)%7]
        
    
    return answer