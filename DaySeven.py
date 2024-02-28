list_data = [i for i in range(1, 13) if i % 2 == 0]

for i in list_data:
    if i % 3 == 0:
        list_data.remove(i)
print(list_data)

for i in range(1, 10):
    if 0 < i < 4:
        list_data.append(i)
print(list_data)

for i in range(8, 5, -1):
    if 5 < i < 9:
        list_data.insert(3, i)

print(list_data)

for i in range(len(list_data)):
    if list_data[i] % 2 == 0 or list_data[i] % 5 == 0:
        list_data[i] = 0



print(list_data)
