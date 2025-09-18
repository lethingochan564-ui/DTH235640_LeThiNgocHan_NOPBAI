import time
n = 3  # số dòng trên (tam giác nhỏ)

# Vẽ phần tam giác trên
for i in range(1, n+1):
    print("      " + "* " * i)

# Vẽ dòng ngang dài
print("* " * 7)

# Vẽ cột giảm dần bên dưới
for i in range(n, 0, -1):
    print("* " * i)

time.sleep(5)

n = 3  # chiều cao phần tam giác trên

# Vẽ tam giác rỗng
for i in range(1, n+1):
    if i == 1:
        print("      *")
    elif i == n:
        print("      *   *")
    else:
        print("      * *")

# Hàng ngang dài
print("* " * 7)

# Cột giảm dần
print("*   *")
print("* *")
print("*")

time.sleep(5)

n = 4  # độ cao tam giác trên

# Tam giác ngược trên
for i in range(n, 0, -1):
    print("      " + "* " * i)

# Tam giác thường dưới
for i in range(2, n+1):
    print("  " * (n-i) + "* " * i)

time.sleep(5)

n = 4  # chiều cao phần trên

# Hàng ngang đầu tiên
print("      " + "* " * n)

# Tam giác rỗng giảm dần
print("      *   *")
print("      * *")
print("      *")

# Tam giác thường ở dưới
print("    * *")
print("  *   *")
print("* * * *")


