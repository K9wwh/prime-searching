n=1;print(*[(n:=next(m for m in range(n+2,2*n+4,2) if all(m%q for q in range(3,int(m**.5)+1,2)))) for _ in range(100000)],sep="\n")
