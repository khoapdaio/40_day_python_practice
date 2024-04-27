# Day 18

# 1: Trong NLP, chúng ta cần loại bỏ 1 số từ không quan trọng (stopwords) ra khỏi câu để tránh gây nhiễu trong việc xử lý. Hãy loại bỏ các từ trong stop_ words =["I","love","and","to" ] câu đầu vào "I love AI and listen to music". Hãy áp dụng List comprehension và for truyền thống để thực hiện

stop_words =["I","love","and","to" ]
word ="I love AI and listen to music"


print([i for i in word.split(' ') if i not in stop_words])

#
# - 3.1: Tạo mới hai tuple: my_tuple=(2,3) , my_tuple2=(3,6) mỗi Tuple có 2 phần tử đại diện cho một vector trong không gian 2D
# - 3.2: in ra kết quả của tổng và tích 2 vector trên
# - 3.3: in ra kết quả của khoảng cách của hai vector trên theo công thức biết distance(p,q)
# - 3.4 in ra vị trí của phần tử có giá trị là 3



import math

my_tuple=(2,3)
my_tuple2=(3,6)

result_vector1 = (my_tuple[0]+my_tuple[1],my_tuple[0]*my_tuple[1])
result_vector2 = (my_tuple2[0]+my_tuple2[1],my_tuple2[0]*my_tuple2[1])
print(f"result_vector1= {result_vector1}")
print(f"result_vector2= {result_vector2}")


distance= math.sqrt((math.pow(my_tuple[0]-my_tuple2[0],2))+(math.pow(my_tuple[1]-my_tuple2[1],2)))
print(f"distance(my_tuple,my_tuple2) = {distance}")


print(f"index = {my_tuple.index(3)}")



