# list(map()) : 각 요소에 특정 함수를 적용한 결과를 새로운 리스트로 변환
# lambda 매개변수 : 표현식 , 인자 
def solution(arr, k):
    if k % 2 != 0:
        return list(map(lambda x: x * k, arr))

    return list(map(lambda x: x + k, arr))
