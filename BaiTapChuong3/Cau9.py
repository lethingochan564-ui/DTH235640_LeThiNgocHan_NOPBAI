month = int(input("Nhập tháng (1-12): "))
if 1 <= month <= 3:
    quarter = 1
elif 4 <= month <= 6:
    quarter = 2
elif 7 <= month <= 9:
    quarter = 3
elif 10 <= month <= 12:
    quarter = 4
else:
    quarter = None
if quarter:
    print(f"Tháng {month} thuộc quý {quarter} trong năm!")
else:
    print("Tháng hông hợp lệ! Vui lòng nhập từ 1 đến 12 nha quý zị.")