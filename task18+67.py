f = open('0067_triangle.txt')
dp = [int(f.readline())]
i = 2https://github.com/Erufaku/euler/tree/main
for line in f:
    s = list(map(int, line.split()))
    newdp = [0] * i
    newdp[0] = dp[0] + s[0]
    for j in range(i - 1):
        newdp[j] = max(dp[j - 1], dp[j]) + s[j]
    newdp[i - 1] = dp[i - 2] + s[i - 1]
    dp = newdp[:]
    i += 1
print(max(dp))
