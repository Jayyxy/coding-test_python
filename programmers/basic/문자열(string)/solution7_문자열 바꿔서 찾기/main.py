def solution(myString, pat):
    myString = myString.lower().replace("a","B").replace("b","A")
       
    if pat in myString : 
           return 1
    return 0