def solution(n):
    result = [] 
    
    # TypeError: 'int' object is not iterable
    # 원인 : result += n 
    # -> 리스트 += 사용시 우측에도 똑같이 반복 가능한 튜플형태가 와야함

    for i in range(n) : 
        result.append(n)
        
        if n % 2 ==0 :
            n /= 2 
        else :
            n = 3 * n + 1   
        
        if n == 1 :
            result.append(n)
            break 
    
    return result