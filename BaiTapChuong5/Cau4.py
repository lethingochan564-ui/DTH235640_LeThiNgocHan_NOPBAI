
s = input("Nhập chuỗi: ")

print("\n--- Kết quả xử lý ---")


print("Độ dài chuỗi:", len(s))


print("strip():", s.strip())


print("lower():", s.lower())
print("upper():", s.upper())


print("capitalize():", s.capitalize())
print("title():", s.title())


words = s.split()
print("split():", words)
print("join():", " ".join(words))


print("replace():", s.replace("a", "@"))


print("find('a'):", s.find("a"))


print("startswith('H'):", s.startswith("H"))
print("endswith('!'):", s.endswith("!"))


print("isdigit():", s.isdigit())
print("isalpha():", s.isalpha())
print("isalnum():", s.isalnum())