class Solution:
    def print2largest(self, arr, n):
        for x in range(-1, -n - 1, -1):
            print(arr[x], end=" ")


if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.print2largest(arr, n)
        tc -= 1
