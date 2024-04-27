import math

def giai_phuong_trinh_bac_hai(a, b, c):
    if a == 0:
        if b == 0 and c == 0:
            return "Phương trình có vô số nghiệm"
        elif b == 0:
            return "Phương trình vô nghiệm"
        else:
            x = -c / b
            return f"Phương trình có một nghiệm: x = {x}"
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            return "Phương trình không có nghiệm thực"
        elif delta == 0:
            x = -b / (2*a)
            return f"Phương trình có nghiệm kép x = {x}"
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}"

print(giai_phuong_trinh_bac_hai(1,10,1))