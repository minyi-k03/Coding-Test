def solution(sides):
    answer = 0
    sum_sides=sum(sides)
    lst=[i for i in range(max(sides),sum_sides) if max(sides)<i<sum(sides)]
    lst2=[i for i in range(1,max(sides)+1) if i+min(sides)>max(sides)]
    
    
    
    
    return len(lst)+len(lst2)