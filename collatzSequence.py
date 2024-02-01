# longest Collatz Sequence
def collatz(n):
    while n != 1:
        print(n, end=' ')
        if n & 1:
            n = n * 3 + 1
        else:
            n = n // 2
    print(n)

x = int(input())
collatz(x)
