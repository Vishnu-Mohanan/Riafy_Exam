n = int(input("Enter the size"))
a = [0]*n
for i in range(n):
    for j in range(n):
        a[i][j] =  list(map(int, input("Input value")))

sum = []

for k in range(n):
    for x,y in k,k:
        sum+=a[x][y]

print(sum)