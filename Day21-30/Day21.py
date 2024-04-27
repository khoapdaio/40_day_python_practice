# Day 21

# Câu 1: hãy đọc file data1.text có trong dataset phía trên và lưu vào biến data sau khi loại bỏ các ký tự \n và thay thế bằng khoảng trắng, đồng thời chuyển về chữ cái thường toàn bộ văn bản


with open("/content/drive/MyDrive/Colab Notebooks/data_1.txt", "r") as f:
	data = f.read()
	data = data.replace("\n", "").split(" ")
	data = [i.lower() for i in data]
	distinct_words = set(data)

print(" ".join(data))

# Câu 2: Phân tích văn bản trên và lưu vào biến có tên distinct_words các chữ cái duy nhất trong câu

print(distinct_words)

# Câu 3: Đếm số lần từng chữ trong distinct_words xuất hiện trong văn bản và cho biết chữ nào xuất hiện nhiều nhất và ít nhất

temp = [[0, ""] for i in range(len(distinct_words))]

distinct_words = list(distinct_words)

max_index, max_value = 0, 0
min_index, min_value = 1, 0

for i, element in enumerate(distinct_words):
	count_e = data.count(element)
	temp[i] = count_e
	print(f"\"{element}\" in data is {count_e} ")
	if max_value < count_e:
		max_index, max_value = i, count_e
	if min_value >= count_e:
		min_index, min_value = i, count_e

print(f"\"{distinct_words[max_index]}\" is most frequent word  ")

print(f"\"{distinct_words[min_index]}\" is lest common word ")
