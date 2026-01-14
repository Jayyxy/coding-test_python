def solution(str_list, ex):
    # 문자열 연결 -> ''.join() 사용
    return ''.join(filter(lambda x: ex not in x, str_list))
    # 또는 return ''.join([s for s in str_list if ex not in s])