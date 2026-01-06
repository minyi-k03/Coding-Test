def solution(survey, choices):
    answer = ''
    choice_score={1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    character={"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    
    
    for i in range(len(survey)):
        
        if 5<=choices[i]<=7:
            character[survey[i][1]]+=choice_score[choices[i]]
        elif 1<=choices[i]<=3:
            character[survey[i][0]]+=choice_score[choices[i]]
            
    character_items=list(character.items())
    
    print(character_items)
    
    while len(answer)!=4:
        if character_items[0][1]>character_items[1][1]:
            answer+=character_items[0][0]
            character_items.pop(0)
            character_items.pop(0)
        elif character_items[0][1]<character_items[1][1]:
            answer+=character_items[1][0]
            character_items.pop(0)
            character_items.pop(0)
        elif character_items[0][1] == character_items[1][1]:
            if ord(character_items[0][0])>ord(character_items[1][0]):
                answer+=character_items[1][0]
                character_itmes.pop(0)
                character_items.pop(0)
            elif ord(character_items[0][0])<ord(character_items[1][0]):
                answer+=character_items[0][0]
                character_items.pop(0)
                character_items.pop(0)
    
    return answer