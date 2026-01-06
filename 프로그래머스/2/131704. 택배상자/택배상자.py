def solution(order):
    answer = 0
    container = [] #보조 컨테이너
    truck = [] #택배상자를 담을 트럭
    order_idx = 0
    box_idx = 1
    
    while box_idx <= len(order):
        container.append(box_idx)
        while container and container[-1] == order[order_idx]:
            answer += 1
            container.pop()
            order_idx += 1
            
        box_idx += 1
        
    return answer