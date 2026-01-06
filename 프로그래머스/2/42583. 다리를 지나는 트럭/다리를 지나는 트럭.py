def solution(bridge_length, weight, truck_weights):
    answer = 0
    sec = 0
    bridge = [0]*bridge_length
    current_weight = 0
    
    while len(truck_weights) > 0:
        sec+=1
        current_weight = current_weight-bridge.pop(0)
        
        if current_weight+truck_weights[0]<=weight:
            current_weight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
            
        else: #current_weight + truck_weights[0] > weight
            bridge.append(0)
    
        
    sec+=bridge_length
    
    return sec