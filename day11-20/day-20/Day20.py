# Day 20

# Mục tiêu: giới thiệu sơ bộ hai thư viện thư viện newspapaer3k, nltk
#
# - b1: cài đặt hai thư viện
# - b2: lấy nội dung từ một trang web thuộc thể loại bài báo bất kỳ
# - b3: in thông tin bài báo
# - b4: in lên toàn bộ ảnh của bài báo
# - b5: sử dụng thư viện nltk để gắn nhãn các từ được tìm thấy trong bài báo đó
#
# !pip install newspaper3k
# !pip install nltk


from newspaper import Article
article= Article('https://vnexpress.net/ky-su-phan-mem-ai-dau-tien-tren-the-gioi-4722040.html')

article.download()
article.parse()


print(article.text)

print(article.images)

import nltk

from nltk.tokenize import word_tokenize

nltk.download('averaged_perceptron_tagger')
data = article.text
tokenization = word_tokenize(data)
result = nltk.pos_tag(tokenization)

print(result)
