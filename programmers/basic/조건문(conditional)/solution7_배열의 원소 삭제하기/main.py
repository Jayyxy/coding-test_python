# 문제 : arr.remove(i)이후 다시 for문으로 돌아갔을때 오류 발생 
#    for i in arr : 
#        if i in delete_list :
#            arr.remove(i)
    # delete_list = set(delete_list)

def solution(arr, delete_list):
    for i in delete_list:
        if i in arr:
            arr.remove(i)
    return arr