def solution(num_list, n):
    answer = []
    
    i = 0
    
    for i in range(n) : 
        
    # =======================================
    # TypeError: 'int' object is not iterable
    # =======================================
    # 원소를 리스트에 추가할 경우 .append 사용
    # answer += num_list[i] -> 리스트에 넣을경우 묶음으로 
    # [num_list[i]]
        answer.append(num_list[i])
        
    return answer
