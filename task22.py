f = open("0022_names.txt")
mass = f.read().split(',')
mass.sort()
print(sum((i + 1) * sum(map(lambda x: ord(x) - 64, mass[i][1:-1])) for i in range(len(mass))))
