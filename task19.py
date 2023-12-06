months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 3
c = 0
for year in range(1901, 2001):
    month = 1
    while month < 13:
        if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            day += (months[month] + 1)
        else:
            day += (months[month])
        month += 1
        if day % 7 == 0:
            c += 1
print(c)
