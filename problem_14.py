##
## The following iterative sequence is defined for the set of positive integers:
##
##      n → n/2 (n is even)
##      n → 3n + 1 (n is odd)
##
## Using the rule above and starting with 13, we generate the following sequence:
##          13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
##
## It can be seen that this sequence (starting at 13 and finishing at 1)
## contains 10 terms. Although it has not been proved yet (Collatz Problem),
## it is thought that all starting numbers finish at 1.
##
## Which starting number, under one million, produces the longest chain?
##
## NOTE: Once the chain starts the terms are allowed to go above one million.

def solve():
    temp = list()
    col = 0
    high_len = 0
    high_val = 0
    for i in range(1000000, 0, -1):
        del temp[:]
        col = i
        temp.append(i)
        while col != 1:
            if col % 2 == 0:
                temp.append(col / 2)
                col = col / 2
            else:
                col = (3 * col) + 1
                temp.append(col)
 
        if high_len < len(temp):
            high_val = i
            high_len = len(temp)
            print('high len: ' + str(high_len) + ' value: ' + str(high_val))


if __name__ == '__main__':
    solve()
