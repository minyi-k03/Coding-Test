def rank(count):
    return 6 if count<2 else 7-count

def solution(lottos, win_nums):
    answer = []
    
    win_count=0
    zero_count=0
    
    for i in lottos:
        if i in win_nums:
            win_count+=1
        elif i==0:
            zero_count+=1
            
            
    min_rank=rank(win_count)    
    max_rank=rank(win_count+zero_count)
    
    answer=[max_rank,min_rank]
            
    
    return answer