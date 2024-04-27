# Day 27

# underthesea là một bộ công cụ mã nguồn mở hỗ trợ xử lý ngôn ngữ tự nhien tiếng việt nlp. Nó được phát triển bởi cộng đồng nghiên cứu nlp tại việt nam và được công vố lần đầu tiên vào năm 2017
#
# !pip install underthesea

from underthesea import pos_tag
from underthesea import classify
from underthesea import sentiment
from underthesea import sent_tokenize
from underthesea import word_tokenize

sentence = "Công cụ Suno AI nhanh chóng nhận được sự chú ý từ người dùng khi có thể tạo bài hát chỉ với vài câu lệnh. Phiên bản mới nhất, V3 Alpha mới được giới thiệu cuối tháng 2, có bản miễn phí với 10 bài hát mỗi ngày"

print(f"""
pos_tag ={pos_tag(sentence)}

classify ={classify(sentence)}

sentiment ={sentiment(sentence)}

sent_tokenize ={sent_tokenize(sentence)}

word_tokenize ={word_tokenize(sentence)}
""")



