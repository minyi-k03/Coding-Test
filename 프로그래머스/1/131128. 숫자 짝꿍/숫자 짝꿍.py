def solution(X, Y):
    answer = ''
    num_set=[]
    XY_set=list(set(X)&set(Y))
    for i in XY_set:
        if X.count(i)==Y.count(i):
            for j in range(X.count(i)):
                num_set.append(i)
                
        elif X.count(i)>Y.count(i):
            for j in range(Y.count(i)):
                num_set.append(i)
        
        elif X.count(i)<Y.count(i):
            for j in range(X.count(i)):
                num_set.append(i)
            
    num_set.sort(reverse=True)
    
    if len(num_set)==0:
        return "-1"
    elif num_set[0]=="0":
        return "0"
    else:
        return "".join(num_set)
    
    