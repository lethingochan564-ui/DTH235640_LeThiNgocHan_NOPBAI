def read_number(a: int, natural: bool = True) -> str:
    unit = {
        0: "",
        1: "Muoi",
        2: "Tram",
        3: "Nghin",
        4: "Muoi Nghin",
        5: "Tram Nghin",
        6: "Trieu",
        7: "Muoi Trieu",
        8: "Tram Trieu",
        9: "Ty",
    }
    number = {
        0: "Khong",
        1: "Mot",
        2: "Hai",
        3: "Ba",
        4: "Bon",
        5: "Nam",
        6: "Sau",
        7: "Bay",
        8: "Tam",
        9: "Chin",
    }

    if a == 0:
        return "Khong"

    result = ""
    i = 0
    while a > 0:
        digit = a % 10
        if digit != 0:
            part = number[digit] + " " + unit[i]
            result = part.strip() + " " + result
        a //= 10
        i += 1

    result = result.strip()
    if natural:
        result = (
            result.replace("Mot Muoi", "Muoi")
                  .replace("Muoi Nam", "Muoi Lam")
                  .replace("Muoi Mot", "Muoi Mot")
                  .replace("Mot Nghin Mot", "Mot Nghin Le Mot")
                  .replace("Mot Trieu", "Mot Trieu")
        )
    return result
print(read_number(15))
print(read_number(15, True))

print(read_number(1001))
print(read_number(1010, True))