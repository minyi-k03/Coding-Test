def solution(skill, skill_trees):
    answer = 0
    skill = list(skill) #스킬 리스트화
    cnt = 0
    
    for i in skill_trees:
        cnt = 0
        stack = [] #스택 초기화
        for j in i:
            if j in skill:
                stack.append(j)
            
        if len(stack) < len(skill):
            for j in range(len(stack)):
                if stack[j]!=skill[j]:
                    break
                elif stack[j] == skill[j]:
                    cnt += 1
            if cnt == len(stack):
                answer +=1
            
        else:
            for j in range(len(skill)):
                if stack[j]!=skill[j]:
                    break
                elif stack[j] == skill[j]:
                    cnt += 1
                    
            if cnt == len(stack):
                answer += 1
            
        
    
    
    return answer