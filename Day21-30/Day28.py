#Day 28

# Thư viện Translate là một thư viện mã nguồn mở được phát triển bởi Google. Nó cho phép ạn dịch văn bản, tài liệu và trang web sang nhiều ngôn ngữ khác nhau. Thư viện này sử dụng công nghệ dịch máy của google, được đào tạo trên một lượng lớn dữ liệu ngôn ngữ
#
# Bài tập: hãy thực hiện dịch hai câu sau với 2 ngôn ngữ: Anh, Nhật sử dụng cả 2 thư viện:
#
# !pip install translate
# !pip install googletrans==4.0.0rc1

sentence= "Công cụ Suno AI nhanh chóng nhận được sự chú ý từ người dùng khi có thể tạo bài hát chỉ với vài câu lệnh. Phiên bản mới nhất, V3 Alpha mới được giới thiệu cuối tháng 2, có bản miễn phí với 10 bài hát mỗi ngày"

from translate import Translator

transolator= Translator(to_lang="vi")
transolation =transolator.translate(sentence)
print(transolation)
transolator= Translator(to_lang="ja")
transolation =transolator.translate(sentence)
print(transolation)

from googletrans import Translator

transolator= Translator()

transolation =transolator.translate(sentence,dest='ja')
print(transolation)
print(transolation.text)

transolation =transolator.translate(sentence,dest='vi')
print(transolation)
print(transolation.text)