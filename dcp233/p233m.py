# Problem #233 [easy]. This problem is asked by Apple.
# Implement the function `fib(n)`, which returns the `n-th` number in the
# Fibonacci sequence, using only `O(1)1 space.


def fib(n, imno=0):
    imno = fib.__name__ + "_r" + str(imno)
    import p233m
    return getattr(p233m, imno)(n)


def fib_r0(n: "integer") -> "integer":
    return fib_r0(n-1) + fib_r0(n-2) if n != 1 and n != 0 else n


def fib_r1(n):
    if n == 1 or n == 0:
        return n
    temp = [0, 1]
    for i in range(2, n+1):
        temp[i % 2] = sum(temp)
    return max(temp)