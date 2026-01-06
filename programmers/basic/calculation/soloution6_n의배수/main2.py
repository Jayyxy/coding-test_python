def solution(num, n):
    return int(not(num % n))

# num%n 값에 not이 붙이면 T/F으로 반환 
# 1) num%n 값이 0이면 False 아니면 True 반환 
# 2) not으로 bool 변환 
# 3) bool값을 int로 변환 

