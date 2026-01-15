def solution(str1, str2):
    answer = ""
    # 2개의 리스트를 한번에 for문으로 실행 -> zip
    
    for a,b in zip(str1,str2) :
        answer += a
        answer += b 
    return answer