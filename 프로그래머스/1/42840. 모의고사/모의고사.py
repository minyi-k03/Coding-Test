#각 패턴 길이 만큼 나누어야 하는데 나누지 않아서 런타임 에러 난듯 
#구조적인 구현은 맞음
def solution(answers):
    answer = []
    people1_pattern=[1,2,3,4,5]
    people2_pattern=[2,1,2,3,2,4,2,5]
    people3_pattern=[3,3,1,1,2,2,4,4,5,5]
    correct=[0,0,0]
    
    for idx,val in enumerate(answers):
        if people1_pattern[idx%len(people1_pattern)]==val:
            correct[0]+=1
        if people2_pattern[idx%len(people2_pattern)]==val:
            correct[1]+=1
        if people3_pattern[idx%len(people3_pattern)]==val:
            correct[2]+=1
    
    for idx,val in enumerate(correct):
        if val==max(correct):
            answer.append(idx+1)
    
    return answer