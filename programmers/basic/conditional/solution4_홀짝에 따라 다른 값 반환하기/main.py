
# 작성 코드 
def solution(n):
    
    answer = 0
    a = 0 
    
    for i in range(n) : 
        if n % 2 != 0 :
            answer += n - a 
        else :
            answer += (n-a)**2

        a = a+2 
    
        if a >= n :
            break
            
        
   
    

    return answer


# 보완 사항 
# : if a>n : break와 a = a+2 대신 range로 범위 및 증가수 설정
