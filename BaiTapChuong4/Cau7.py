import math
Xa = int(input ("Nhap toa do Xa:"))
Xb = int(input ("Nhap toa do Xb:"))
Ya = int(input ("Nhap toa do Ya:"))
Yb = int(input ("Nhap toa do Yb:"))
AB= math.sqrt((Xb-Xa)*(Xb-Xa)+(Yb-Ya)*(Yb-Ya))
Kết_quả = abs(AB)
print("AB =", AB)