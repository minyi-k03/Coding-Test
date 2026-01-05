def solution(sides):
   
    max_num=max(sides)
    sides.remove(max_num)
    min_num=0
    
    for i in sides:
        min_num+=i
        
    if min_num<=max_num:
        return 2
    elif min_num>max_num:
        return 1
    
    
    
    