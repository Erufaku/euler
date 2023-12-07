sss = {}
for num in range(2, 10000):
    s = 1
    for d in range(2, int(num ** (1/2))):
        if num % d == 0:
            s += d + num // d
    if int(num ** (1/2)) * int(num ** (1/2)) == num:
        s += int(num ** (1/2))
    sss[num] = s
c = 0
for k in sss:
    if 1 < sss[k] <= 10000:
        if sss[k] != k and k == sss[sss[k]]:
            c += sss[k] + sss[sss[k]]
print(c // 2)
