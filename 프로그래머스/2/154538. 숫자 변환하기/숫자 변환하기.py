from collections import deque
def solution(x, y, n): #BFS사용하여 문제풀이
    answer = 0
    queue = deque([(x,0)]) #시작 값,노드
    visited = {x} #방문 노드 처리
    
    while queue:
        current_num,count = queue.popleft()
        
        if current_num == y: #답에 근접했을때
            return count #계산 횟수 리턴
        
        next_nums = [current_num+n,current_num*2,current_num*3] #next_nums에 연산들을 리스트에 넣음
        
        for next_num in next_nums: #리스트 순회
            if next_num <= y and next_num not in visited: #현재 순회 값이 찾는값 y를 넘지 않고 방문 하지 않았다면
                queue.append((next_num,count+1)) #큐에 해당 값 추가
                visited.add(next_num) #방문 노드에 추가
    
    
    
    return -1