def solution(ineq, eq, n, m):
    eqs = ineq + eq
    
    if eqs == ">=" :
        return int(n>=m)
    elif eqs == "<=" :
        return int(n<=m)
    elif eqs == ">!":
        return int(n>m)
    elif eqs == "<!" :
        return int(n<m)