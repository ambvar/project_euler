## The sequence of triangle numbers is generated by adding the natural numbers.
## So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
## The first ten terms would be:
##
## 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
##
## Let us list the factors of the first seven triangle numbers:
##
##     1: 1
##     3: 1,3
##     6: 1,2,3,6
##    10: 1,2,5,10
##    15: 1,3,5,15
##    21: 1,3,7,21
##    28: 1,2,4,7,14,28
##
## We can see that 28 is the first triangle number to have over five divisors.
##
## What is the value of the first triangle number to have over five hundred divisors?

def solve ():
    tri_num, i =  0, 20

    while True:
        divisors = 1
        tri_num =  int(i * (i + 1) / 2)
        for k in range(1, tri_num):
            if tri_num % k == 0:
                divisors += 1


        if divisors >= 500:
            print(tri_num)
            break
        else:
            i += 1
    
    
        
    print('Triangle Number: ' + str(tri_num) + ' Divisors: ' + str(divisors))


if __name__ == '__main__':
    solve()
    
