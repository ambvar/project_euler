import datetime

def solve():
    sundays = 0

    for i in range(1901, 2001):
        for j in range(1, 13):
            if datetime.datetime(i, j, 1).weekday() == 6:
##                print("year: " + str(i) + " month: " + str(j))
                sundays += 1
    


    print(sundays)

if __name__ == "__main__":
    solve()
