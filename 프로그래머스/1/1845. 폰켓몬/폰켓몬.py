from itertools import combinations
def solution(nums):
    total_nums=int(len(nums)//2)
    set_nums=list(set(nums))
    
    if total_nums==len(set_nums):
        return len(set_nums)
    elif total_nums<len(set_nums):
        return total_nums
    elif total_nums>len(set_nums):
        return len(set_nums)
    
    
    