def solution(my_string, overwrite_string, s):
    # 아래 처럼 슬라이스로 할당 불가능 TypeError 발생 
    # my_string[s:n] = overwrite_string
    
    return my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]