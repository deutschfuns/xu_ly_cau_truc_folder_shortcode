# import os

# # Thay đổi đường dẫn này thành đường dẫn đến thư mục gốc của bạn
# root_directory = 'course_'

# course_count = 0
# lesson_count = 0
# topic_count = 0
# shortcode_count = 0
# video_folder_count = 0
# shortcode_file_count = 0

# # Duyệt qua cây thư mục
# for dirpath, dirnames, filenames in os.walk(root_directory):
#     for dirname in dirnames:
#         if 'course' in dirname.lower():
#             course_count += 1
#         elif 'lesson' in dirname.lower():
#             lesson_count += 1
#         elif 'topic' in dirname.lower():
#             topic_count += 1
#         elif 'shortcode' in dirname.lower():
#             shortcode_count += 1
#         elif 'video' in dirname.lower():
#             video_folder_count += 1

#     for filename in filenames:
#         if filename.endswith('.txt'):
#             shortcode_file_count += 1

# # In kết quả
# print(f'Số thư mục course: {course_count}')
# print(f'Số thư mục lesson: {lesson_count}')
# print(f'Số thư mục topic: {topic_count}')
# print(f'Số thư mục shortcode: {shortcode_count}')
# print(f'Số thư mục video: {video_folder_count}')
# print(f'Số file shortcode (.txt): {shortcode_file_count}')

import os
import re

# Thay đổi đường dẫn này thành đường dẫn đến thư mục gốc của bạn
root_directory = 'course_'

course_count = 0
lesson_count = 0
topic_count = 0
shortcode_count = 0
video_folder_count = 0
shortcode_file_count = 0
shortcode_invalid_count = 0
shortcode_invalid_paths = []  # Danh sách lưu trữ đường dẫn không đúng định dạng

# Duyệt qua cây thư mục
for dirpath, dirnames, filenames in os.walk(root_directory):
    for dirname in dirnames:
        if 'course' in dirname.lower():
            course_count += 1
        elif 'lesson' in dirname.lower():
            lesson_count += 1
        elif 'topic' in dirname.lower():
            topic_count += 1
        elif 'shortcode' in dirname.lower():
            shortcode_count += 1
            # Kiểm tra xem tên thư mục có phù hợp với định dạng "shortcode_<số>" hay không
            if not re.match(r'shortcode_\d+', dirname.lower()):
                shortcode_invalid_count += 1
                shortcode_invalid_paths.append(os.path.join(dirpath, dirname))  # Lưu đường dẫn không hợp lệ
        elif 'video' in dirname.lower():
            video_folder_count += 1

    for filename in filenames:
        if filename.endswith('.txt'):
            shortcode_file_count += 1

# In kết quả
print(f'Số thư mục course: {course_count}')
print(f'Số thư mục lesson: {lesson_count}')
print(f'Số thư mục topic: {topic_count}')
print(f'Số thư mục shortcode: {shortcode_count}')
print(f'Số thư mục shortcode không đúng định dạng: {shortcode_invalid_count}')

# Liệt kê đường dẫn của các thư mục shortcode không đúng định dạng
if shortcode_invalid_paths:
    print('Đường dẫn các thư mục shortcode không đúng định dạng:')
    for path in shortcode_invalid_paths:
        print(path)
else:
    print('Không có thư mục shortcode nào không đúng định dạng.')