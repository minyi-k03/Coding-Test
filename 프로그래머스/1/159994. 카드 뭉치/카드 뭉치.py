def solution(cards1, cards2, goal):
    answer = ''
    stack=[]
    
    for i in goal:
        if i in cards1 and cards1.index(i)==0:
            stack.append(i)
            cards1.pop(0)
        elif i in cards2 and cards2.index(i)==0:
            stack.append(i)
            cards2.pop(0)
    
    if stack==goal:
        return "Yes"
    else:
        return "No"
    