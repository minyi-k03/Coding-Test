def solution(n, words):
    answer = []
    stack = [] 
    recursive = 0 #순회
    count = 1
    for i in range(len(words)):
        
        recursive+=1
        
        if len(stack) == 0: #스택이 비어 있는 경우
            stack.append(words[i])
            
            
            
        elif len(stack) != 0 and words[i] not in stack and words[i][0] == stack[-1][-1]:
            stack.append(words[i])
            
            
            
        elif words[i] in stack or words[i][0] != stack[-1][-1]: #끝말잇기에서 틀린경우
            return [recursive,count]
        
        
        
        
        if recursive == n:
            recursive = 0
            count+=1
            
        
            

    return [0,0]