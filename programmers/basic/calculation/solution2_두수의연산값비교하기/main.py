def solution(a, b):
    answer = 0

    #  a ⊕ b와 2 * a * b값을 비교하여 return
    if int(str(a) + str(b)) >= 2 * a * b :
        answer = int(str(a) + str(b))
    else : 
        answer = 2*a*b
    return answer