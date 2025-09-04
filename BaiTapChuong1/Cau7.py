import sys

if len(sys.argv) < 2:
    print("Vui lòng nhập chuỗi cần in dưới dạng tham số dòng lệnh.")
else:
    # Nối tất cả tham số từ argv[1] trở đi thành chuỗi hoàn chỉnh
    chuoi = ' '.join(sys.argv[1:])
    print("Chuỗi đã nhập là:", chuoi)
