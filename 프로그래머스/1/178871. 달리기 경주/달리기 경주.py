def solution(players, callings):
    answer = []
    player_dict={player:idx for idx,player in enumerate(players)}
    
    for i in callings:
        idx=player_dict[i]
        players[idx],players[idx-1]=players[idx-1],players[idx] #players 리스트 내 순서 교환
        player_dict[players[idx]]=idx #딕셔너리 내 등수 입력
        player_dict[players[idx-1]]=idx-1 #딕셔너리 내 등수 입력
        
        
    
    
    
    return players