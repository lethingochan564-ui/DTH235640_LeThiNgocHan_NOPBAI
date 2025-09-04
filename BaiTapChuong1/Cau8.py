width = 4   # chiều ngang
height = 4  # chiều dọc

for i in range(height):
    for j in range(width):
        # nếu là dòng đầu, dòng cuối, hoặc cột đầu, cột cuối -> in '*'
        if i == 0 or i == height - 1 or j == 0 or j == width - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()