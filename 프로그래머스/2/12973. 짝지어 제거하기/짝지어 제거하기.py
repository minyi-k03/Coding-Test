def solution(s):
    
    stack=[]
    
    for i in range(len(s)):
        
        if stack==[]:
            stack.append(s[i])
            continue
            
        top=stack[-1]
        
        if top==s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    
    if stack==[]:
        return 1
    else:
        return 0