def solution(order):
    answer = 0
    
    for i in order:
        if i=="cafelatte" or i=="hotcafelatte" or i=="cafelattehot" or i=="icecafelatte" or i=="cafelatteice":
            answer+=5000
        elif i=="americano" or i=="hotamericano" or i=="americanohot" or i=="iceamericano" or i=="americanoice" or i=="anything":
            answer+=4500
        
    
    return answer