def solution(num_list):
    
    total1=0 #홀수
    total2=0 #짝수
    
    for i in range(1,len(num_list),2): #짝수 
        total2+=num_list[i]
        
    for i in range(0,len(num_list),2): #홀수
        total1+=num_list[i]
        
    if(total2>total1):
        return total2
    else:
        return total1
        
        
    
   