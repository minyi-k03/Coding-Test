def solution(rank, attendance):
    answer = 0
    rank_lst=[]
    for i in range(len(attendance)):
        if attendance[i]:
            rank_lst.append([rank[i],rank.index(rank[i])])
    
    rank_lst.sort()
    
    
    
    return 10000*rank_lst[0][1]+100*rank_lst[1][1]+rank_lst[2][1]