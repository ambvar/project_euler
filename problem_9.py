
high = 0
prod = 0

for i in range(1, 1000):
    for j in range(1, 1000):
        for k in range(1, 1000):
            a = i * i
            b = j * j
            c = k * k
            if (a + b) == c:
                v = i + j + k
                if v == 1000:
                    prod = i * j * k
                    print(str(i) + ' ' + str(j) + ' ' + str(k))
                    print('product: ' + str(prod))
