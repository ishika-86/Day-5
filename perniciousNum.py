def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def pernicious(n):
    i, count = 1, 0
    while count < n:
        if is_prime(bin(i).count('1')):
            print(i, end=' ')
            count += 1

        i += 1


n = int(input())
pernicious(n)
