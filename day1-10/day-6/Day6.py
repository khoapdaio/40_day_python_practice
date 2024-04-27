
# Ví dụ về Switch case python => match case

today= input("Hôm nay là thứ mấy vậy? ")

match today:
  case "Thứ 2":
    print("Ngày đầu tuần")
  case "Thứ 3":
    print("Sau ngày thứ 2 ak")
  case "Thứ 4":
    print("Gần được nửa tuẩn rồi")
  case "Thứ 5":
    print("Được nửa tuần rồi đó")
  case "Thứ 6":
    print("Cuối tuần rồi ")
  case "Thứ 7":
    print("ngày nghỉ đây rồi ")
  case "Chủ nhật":
    print("Thật tuyệt vời")
  case other:
    print("Ngày nào chả được")


# Ví dụ về dictionary

toDos ={
      "Thứ 2":"Ngày đầu tuần",
      "Thứ 3":"Sau ngày thứ 2 ak",
      "Thứ 4":"Gần được nửa tuẩn rồi",
      "Thứ 5":"Được nửa tuần rồi đó",
      "Thứ 6":"Cuối tuần rồi",
      "Thứ 7":"ngày nghỉ đây rồi",
      "Chủ nhật":"Ngày nào chả được"
}

toDos.get(input("Hôm này là thứ mấy vậy? "))