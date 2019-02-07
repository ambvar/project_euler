
divisible = True
val = 5000

while divisible:
    for i in range(1, 21):
        if val % i != 0:
            val = val + 1
            break
        elif i == 20:
            print('we hit it')
            divisible = False
            print(str(val))
            
