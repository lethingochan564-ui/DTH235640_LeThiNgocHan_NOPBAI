def ToiUuChuoiDanhTu(s):
    words = s.strip().split()
    for i in range(len(words)):
        words[i] = words[i].lower().capitalize()
    return " ".join(words)
s = "    TRần    duY   ThANh   "
print("Input :", repr(s))
print("Output:", ToiUuChuoiDanhTu(s))