import math

factors = list()
high = 0

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def main():
    num = 600851475143
    global high
    for i in range(2, num):
        if num % i == 0:
            if i % 2 != 0:
                if is_prime(i):
                    print(i)
            


if __name__ == "__main__":
    main()

