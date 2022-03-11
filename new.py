def printDecreasing(n):
    # write your code here
    if n==0:
        return
    printDecreasing(n-1)
    print(n)

n = int(input())
printDecreasing(n)