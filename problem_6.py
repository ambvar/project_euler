
sum_of_squares = 0
total = 0
square_of_sum = 0
diff = 0

for i in range(1, 101):
    sum_of_squares = (i *i) + sum_of_squares
    total = total + i


square_of_sum = total * total
diff = square_of_sum - sum_of_squares

print(diff)
