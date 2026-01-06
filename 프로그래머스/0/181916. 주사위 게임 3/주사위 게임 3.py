#Git Hub에서 참고함
def solution(a, b, c, d):
    dice=[a,b,c,d]
    non_set_list=list(set(dice))
    
    if len(non_set_list)==1:
        return 1111*non_set_list[0]
    elif len(non_set_list)==2:
        for i in dice:
            if dice.count(i)==3:
                p=i
                q=[x for x in non_set_list if x!=p][0]
                return (10*p+q)**2
            elif dice.count(i)==2:
                p=i
                q=[x for x in non_set_list if x!=p][0]
                return (p+q)*(abs(p-q))
    elif len(non_set_list)==3:
        for i in dice:
            if dice.count(i)==2:
                new_list=[x for x in non_set_list if x!=i]
                return new_list[0]*new_list[1]
            
            
    else:
        return min(dice)
            
                
        
        
                
    
    
    
    
    
    
    

    