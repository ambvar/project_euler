import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


curr = 2
num = 0
ten_thousand = False
while not ten_thousand:
    if is_prime(curr):
        num = num + 1

    if num == 10001:
        print(curr)
        ten_thousand = True

    curr = curr + 1
