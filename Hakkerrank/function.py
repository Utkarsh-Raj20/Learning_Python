n = int(input())
ans = "1"
if n == 1:
    print(ans)
else:   
    i = 2
    while i<=n:
        ans = ans +' '+ str(i)
        i+=1
    print(ans)
        