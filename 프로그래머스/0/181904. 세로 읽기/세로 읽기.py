def solution(my_string, m, c):
    answer = ''
    y=len(my_string)//m
    lst=[]
    
    for i in range(0,len(my_string),m):
        answer+=my_string[i:i+m][c-1]
        
        
        
    return answer