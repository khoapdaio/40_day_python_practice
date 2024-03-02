# nắm được các sử dụng enumerate


# Food List

foodList = [
    ["Bơ", "Pizza", "Sữa"],
    ["Xúc xích", "Táo", "Kem"],
    ["Cà Rốt", "Bánh Dâu", "Cupcake"]
]
search_items = ["Cà rốt", "Táo", "Pizza"]
# Method 1

for i in range(len(foodList)):
    for j in range(len(foodList[i])):
        if foodList[i][j] in search_items:
            print(f"{foodList[i][j]} được tìm thấy"
                  f"thấy ở hàng {i + 1} và cột {j + 1}")

for i, row in enumerate(foodList, start=1):
    for j, item in enumerate(row, start=1):
        if item in search_items:
            print(f"{item} được tìm thấy"
                  f"thấy ở hàng {i} và cột {j}.")
