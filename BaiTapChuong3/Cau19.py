import math
def calculate_S(x, n):
    S = 0
    for i in range(n + 1):
        exponent = 2 * i + 1
        S += (x ** exponent) / math.factorial(exponent)
    return S
# Input values
x = float(input("Hãy nhập vào giá trị của x: "))
n = int(input("Để tiếp tục, hãy nhập vàp giá trị của n: "))
result = calculate_S(x, n)
print(f"Giá trị của S"
      f"({x}, {n}) là: {result}")