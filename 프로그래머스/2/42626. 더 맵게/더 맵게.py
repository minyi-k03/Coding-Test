import heapq

def solution(scoville, K):
    if not scoville:  # 입력 리스트가 비어있는 경우
        return -1

    heapq.heapify(scoville)
    cnt = 0

    while scoville and scoville[0] < K:  # 힙이 비어있지 않고, 최소값이 K보다 작을 때까지
        if len(scoville) < 2:
            return -1
        
        # 섞은 음식을 힙에 넣기 전에 힙이 비어있는지 확인
        if scoville:
            new_food = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
            heapq.heappush(scoville, new_food)
            cnt += 1
        else:
            return -1  # 힙이 비어있으면 -1 반환

    return cnt