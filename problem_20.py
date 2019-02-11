import math

def solve():
    f = str(math.factorial(100))
    s = 0;

    for i in range(0, len(f)):
        s  += int(f[i])


    print(s)


if __name__ == "__main__":
    solve()
