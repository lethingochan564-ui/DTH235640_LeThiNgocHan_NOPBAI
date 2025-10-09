def NegativeNumberInStrings(s):
    result = []
    i = 0
    while i < len(s):
        if s[i] == '-' and i+1 < len(s) and s[i+1].isdigit():
            j = i + 1
            num_str = "-"
            while j < len(s) and s[j].isdigit():
                num_str += s[j]
                j += 1
            result.append(int(num_str))
            i = j 
        else:
            i += 1
    return result

s = "abc-5xyz-12k9l--p"
nums = NegativeNumberInStrings(s)
print("Các số nguyên âm trong chuỗi:", nums)