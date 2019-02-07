prev = 1
next = 2
curr = 0
total = 0

while curr < 4000000:
    curr = prev + next
    prev = next
    next = curr
    print('fib: ' + str(curr))
    if curr % 2 == 0:
        total = total + curr
    print('total: ' + str(total))

