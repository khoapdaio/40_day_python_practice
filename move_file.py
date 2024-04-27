import os
import shutil


def move_files( source_dir, destination_dir, num_days ):
	start_date = 31
	end_date = start_date + 10
	for day in range(start_date, end_date):
		if day not in (24, 25, 32, 33):
			src_day_dir = os.path.join(source_dir, f"Day-{day}")
			dest_day_dir = os.path.join(destination_dir, f"day{start_date}-{end_date-1}\day-{day}")

			if not os.path.exists(src_day_dir):
				continue
			# Tạo thư mục đích nếu chưa tồn tại
			if not os.path.exists(dest_day_dir):
				os.makedirs(dest_day_dir)

			for filename in os.listdir(src_day_dir):
				if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.pdf')):
					src_file_path = os.path.join(src_day_dir, filename)
					dest_file_path = os.path.join(dest_day_dir, f"day-{day}.{filename.split('.')[1]}")
					shutil.copyfile(src_file_path, dest_file_path)


# Đường dẫn của thư mục nguồn và đích
source_directory = "O:\Git\\40-days-basic-python\\"
destination_directory = "O:\Git\personal\\40_day_python_practice\\"
# Số ngày
num_days = 40

move_files(source_directory, destination_directory, num_days)
