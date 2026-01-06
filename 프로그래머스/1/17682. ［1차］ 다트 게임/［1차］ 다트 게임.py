def solution(dartResult):
    answer = []
    stack=''
    
    for dart in dartResult:
        if dart.isnumeric():
            stack+=dart
            
        elif dart == 'S':
            score=pow(int(stack),1)
            answer.append(score)
            stack = ''
            
        elif dart == 'D':
            score = pow(int(stack),2)
            answer.append(score)
            stack = ''
            
        elif dart == 'T':
            score = pow(int(stack),3)
            answer.append(score)
            stack = ''
            
        elif dart == "*":
            if len(answer)>1:
                answer[-2] = answer[-2]*2
                answer[-1] = answer[-1]*2
                
            else:
                answer[-1] = answer[-1]*2
                
        
        elif dart == "#":
            answer[-1] = answer[-1] * -1
                
        
    
    return sum(answer)