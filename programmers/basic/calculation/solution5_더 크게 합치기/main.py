def solution(a, b):

    # if 문 사용시 콜론(:) 잊지말것
    if int(str(a) + str(b)) < int(str(b) + str(a)) :
        return int(str(b) + str(a))
    
    return int(str(a) + str(b))
