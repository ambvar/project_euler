for i in range(100, 999):
    for j in range(100, 999):
        val = i * j
        string = str(val)
        first, second = string[:len(string)//2], string[len(string)//2:]
        sec = second[::-1]
        if first == sec:
            v1 = i
            v2 = j
            print('val 1: ' + str(v1) + ' val 2: ' + str(v2) + ' equals: ' + str(v1 * v2))



print ('val 1: ' + str(v1) + ' val 2: ' + str(v2))

