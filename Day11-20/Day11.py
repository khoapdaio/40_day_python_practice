# Bag of words là một thuật toán hỗ trợ xử lý ngôn ngữ tự nhiên và mục đích của bơ là phân loại text hay văn bản.
# Ý tưởng của BoW là phân tích và phân nhóm dựa theo "Bag of Words " corpus. Với test data mới,
# tiến hành tìm ra số lần từng từ của test data xuất hiện trong "Bag".


corpus=[
    "Tôi thích môn toán",
    "Tôi thích AI",
    "Tôi thích âm nhạc"
]

# Bước 1: Chia nhỏ văn bản thành các từ riêng lẻ
# Bước 2: Tạo một tập hợp các từ xuất hiện trong văn bản. Tập hợp này không có phần tử trùng nhau
def getVocabulary(tokens):
  result= set()
  for s in tokens:
    for c in s.split(" "):
      result.add(c)
  return result
vocabulary= getVocabulary(corpus)
print(vocabulary)

# Bước 3: Biểu diễn văn bản input ở dạng vector: Mỗi câu (mỗi input) được biểu diễn bằng một vector,
# với mỗi phần tử trong vector thể hiện số lần xuất hiện của tờ đó trong input

def getBagOfWords(strInput, voca):
  strInput= strInput.split(" ")
  return [strInput.count(x) for x in voca]

print(getBagOfWords("Tôi thích AI thích toán",vocabulary))