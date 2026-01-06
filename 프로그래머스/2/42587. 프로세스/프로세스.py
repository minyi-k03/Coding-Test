def solution(priorities, location):
    answer = 0
    queue = [[idx, val] for idx, val in enumerate(priorities)]  # 작업 목록 (인덱스, 우선순위)
    
    while queue:  # 큐가 비어있을 때까지 반복
        current, priority = queue.pop(0)  # 현재 작업 가져오기
        
        # 더 높은 우선순위 작업이 남아있는 경우 뒤로 이동
        if any(p > priority for _, p in queue):
            queue.append([current, priority])
        else:
            answer += 1
            if current == location:  # 찾는 문서인 경우
                break

    return answer