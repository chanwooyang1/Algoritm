def star(n):
    if n == 1:
        return ["*"]

    Stars = star(n//3)
    L = []
    
    for s in Stars:
        L.append(s*3)
    for s in Stars:
        L.append(s + " " * (n // 3) + s)
    for s in Stars:
        L.append(s*3)
    
    return L



N = int(input())
print("\n".join(star(N)))
