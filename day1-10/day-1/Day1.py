def calculate_can_chi_calendar(namSinh):
    danhSachCan = {0: "Canh", 1: "Tân", 2: "Nhâm", 3: "Quý", 4: "Giáp",
                   5: "Ất", 6: "Bính", 7: "Đinh", 8: "Mậu", 9: "Kỷ"}

    danhSachChi = {0: "Thân", 1: "Dậu", 2: "Tuất", 3: "Hợi", 4: "Tý", 5: "Sửu",
                   6: "Dần", 7: "Mẹo", 8: "Thìn", 9: "Tỵ", 10: "Ngọ", 11: "Mùi"}
    return danhSachCan[namSinh % 10] + ' ' + danhSachChi[namSinh % 12]


def get_can(namSinh):
    can = namSinh % 10
    if can == 0:
        return "Canh"
    if can == 1:
        return "Tân"
    if can == 2:
        return "Nhâm"
    if can == 3:
        return "Quý"
    if can == 4:
        return "Giáp"
    if can == 5:
        return "Ất"
    if can == 6:
        return "Bính"
    if can == 7:
        return "Đinh"
    if can == 8:
        return "Mậu"
    if can == 9:
        return "Kỷ"


def get_chi(namSinh):
    chi = namSinh % 12
    if chi == 0:
        return "Thân"
    if chi == 1:
        return "Dậu"
    if chi == 2:
        return "Tuất"
    if chi == 3:
        return "Hợi"
    if chi == 4:
        return "Tý"
    if chi == 5:
        return "Sửu"
    if chi == 6:
        return "Dần"
    if chi == 7:
        return "Mẹo"
    if chi == 8:
        return "Thìn"
    if chi == 9:
        return "Tỵ"
    if chi == 10:
        return "Ngọ"
    if chi == 11:
        return "Mùi"


def get_can_chi(namSinh):
    return get_can(namSinh) + " " + get_chi(namSinh)


print(get_can_chi(1997))
