def solution(number, limit, power):
    answer = 0
    lst=[] #약수들 개수
    tmp=[] #약수들
    count=0
    for i in range(1,number+1):
        for j in range(1,int(i**(1/2))+1):
            if i%j==0:
                count+=1
                tmp.append(j)
                if j**2!=i:
                    count+=1
                    tmp.append(i//j)
        lst.append(count)
        count=0
        
    
    for idx,val in enumerate(lst):
        if val>limit:
            lst[idx]=power
            
    
    
            
    return sum(lst)