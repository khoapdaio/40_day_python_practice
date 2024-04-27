#Day 19

# Câu 1: Tạo List có tên lst_data gồm các số từ 1 đến 10, sau đó ghi toàn bộ list trên vào file có tên: data.txt với nội dung là 1 chuỗi số từ list trên nối với nhau bằng dấu -
#
# Câu 2: Đọc file data.txt vừa tạo ở câu 1 và lưu vào list mới có tên lst_filter gồm các số chia hết cho 3

f =open("/content/drive/MyDrive/Colab Notebooks/data.txt","w")
lst_data ="-".join( str(i) for i in range(1,11))
f.write(f"lst_data={lst_data}")
print(f'lst_data={lst_data}')
f.close()

f = open("/content/drive/MyDrive/Colab Notebooks/data.txt","r")
data=f.read()
f.close()


f = open("/content/drive/MyDrive/Colab Notebooks/data.txt","w")
data = data[data.index("=")+1:].split("-")
lst_filter = [i for i in data if int(i)%3==0]
f.write(f"lst_filter={lst_filter}")
f.close()


print(f'data={data}')
print(f'lst_filter={lst_filter}')

# Phân tích dữ liệu thực đơn của McDonald Hãy đọc file menu.csv có trong dataset phía trên và lưu vào biến data với thư viện Pandas. Sau đó sủ dụng hàm describe(), info(), head(), tail() để thống kê tập dataset. Lưu ý: lấy 5 phần tử đầu tiên và 10 phần tử cuối cùng khi dùng hàm head và tail

import pandas as pd

pf = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/menu.csv')
pf.describe()

pf.info()

pf.head()

pf.tail()