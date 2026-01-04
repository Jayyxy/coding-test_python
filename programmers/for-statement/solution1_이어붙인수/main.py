def solution(num_list):
    answer = 0
    
    i = 0 
    even = ""
    odd = ""
    
    # ==========================================================
    # 'int' object is not iterable
    # ==========================================================
    # - for 문에는 정수(int) 가 아닌 반복 가능한 객체(iterable)가 들어있어야함
    # - len(num_list) -> range(len(num_list)) or num_list
    
    for i in range(len(num_list)) : 
        # 짝수 
        if num_list[i] % 2 == 0 :
            even += str(num_list[i])
            
        # 홀수
        else :
            odd += str(num_list[i])
            
    answer = int(even) + int(odd)
    return answer