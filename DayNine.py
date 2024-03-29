# cách tính trung vị của list và sử dụng hàm sorted

list_item = [i for i in range(1, 10)]
print(list_item)


def tinhTrungVi(items):
    n = len(items)
    if n % 2 == 0:
        return (items[n // 2 - 1] + items[n // 2]) / 2
    return items[n // 2]


print(tinhTrungVi(list_item))

print(sorted([i for i in list_item if i % 2 != 0], reverse=True))
