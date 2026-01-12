def solution(start_num, end_num):
    answer= []
    # 문제1. i = start_num 으로 설정하여도 for 문이 실행되는 순간 i는 range가 생성하는 숫자로 덮어씌워집니다
    # 문제2. range(end_num) -> end_num 이전까지만 반복 
    for i in range(start_num, end_num+1) :
        answer.append(i)
        
        
    return answer