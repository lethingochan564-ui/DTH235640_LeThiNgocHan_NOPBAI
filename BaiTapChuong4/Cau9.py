import math
n = int(input("Nhập n: "))
S = 0
for i in range(1, n + 1):
    S = math.sqrt(i + S)

print("Giá trị căn bậc hai lồng nhau =", S)