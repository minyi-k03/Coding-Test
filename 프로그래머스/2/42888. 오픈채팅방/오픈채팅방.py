def solution(record):
    answer = []
    id_nickname = {} #현실 아이디 가상 닉네임 딕셔너리화
    visited = [] #방문에 대한 기록
    
    for i in record:
        part = i.split(" ")
        visited.append((part[0],part[1]))
        if len(part) >= 3:
            visit = part[0]
            uid = part[1]
            nickname = part[2]
            
            if uid not in id_nickname: #해당 딕셔너리에 아이디랑 닉네임이 없다면
                id_nickname[uid] = i.split(" ")[2]
            else: #있다면 최신화
                id_nickname[uid] = i.split(" ")[2]
        
    for i in visited:
        if i[0] == 'Enter':
            answer.append(id_nickname[i[1]]+"님이 들어왔습니다.")
        elif i[0] == 'Leave':
            answer.append(id_nickname[i[1]]+"님이 나갔습니다.")
    
    
    
    return answer