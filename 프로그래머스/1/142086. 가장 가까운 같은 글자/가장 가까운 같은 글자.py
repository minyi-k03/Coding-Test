#저번에 풀었던 답이랑 거의 정답 접근성은 비슷했지만 rfind()함수를 생각하지 못했음
def solution(s):
    answer = []
    stack=""
    
    for idx,val in enumerate(s):
        if val not in stack:
            answer.append(-1)
            stack+=val
        elif val in stack:
            answer.append(idx-stack.rfind(val))
            stack+=val
            
    
    return answer