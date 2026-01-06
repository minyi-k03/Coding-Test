from collections import deque
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = [] #인덱스 저장 스택
    
    
    for idx,val in enumerate(numbers):
        while stack and numbers[stack[-1]] < val:
            prev_idx = stack.pop()
            answer[prev_idx] = val
            
        stack.append(idx)
                
        
        
    return answer