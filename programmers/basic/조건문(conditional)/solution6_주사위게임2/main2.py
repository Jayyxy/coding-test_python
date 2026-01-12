
def solution(a, b, c):

    # set()의 성질 : 중복을 허용하지 않는 순서없는 데이터 집합
    # -> 값이 같은 경우 len의 길이가 변함
    check=len(set([a,b,c]))
    if check==1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)