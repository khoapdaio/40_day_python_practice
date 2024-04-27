#Day 13

# Bài tập: tìm kiếm giá trị None đầu tiên và tìm kiếm tất cả các vị trí có giá trị None

import random

lst_data = [i for i in range (6000000)]

for i in range(10):
  lst_data[ random.randint(1,6000000)] = None

none_lst_data=[]
for i in range(len(lst_data)-1):
  if lst_data[i] is None:
    none_lst_data.append(i)

print(f"""- Vị trí None đầu tiên:{none_lst_data[0]}
- Danh sách có vị trí có giá trị None:{none_lst_data}
""")
