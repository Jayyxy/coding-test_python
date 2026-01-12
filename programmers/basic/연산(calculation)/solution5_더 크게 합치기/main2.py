
def solution(a, b):
    # max - > 문자열 간에도 비교 가능
    return int(max(f"{a}{b}", f"{b}{a}"))