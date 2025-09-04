h = [1, 3, 5, 3, 7, 9]
max_width = max(h)
for sao in h:
    space = (max_width - sao) // 2
    print(" " * space + "*" * sao)
for _ in range(2):
    space = (max_width - 3) // 2
    print(" " * space + "*" * 3)