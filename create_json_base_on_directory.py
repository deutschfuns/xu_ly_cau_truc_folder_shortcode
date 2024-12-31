# import json

# # Khởi tạo cấu trúc dữ liệu
# data = {
#     "title": "",
#     "id": "",
#     "lessons": []
# }

# # Đọc nội dung từ file muc_luc.txt
# with open('muc_luc.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()

# current_lesson = None

# for line in lines:
#     line = line.strip()
#     if line.startswith("[Course]"):
#         data["title"] = line.replace("[Course]", "").strip()  # Lấy tiêu đề khóa học
#     elif line.startswith("[Lesson]"):
#         if current_lesson:
#             data["lessons"].append(current_lesson)
#         current_lesson = {
#             "title": line.replace("[Lesson]", "").strip(),
#             "id": "",
#             "topics": []
#         }
#     elif line.startswith("[Topic]"):
#         topic = {
#             "title": line.replace("[Topic]", "").strip(),
#             "topic_id": "",
#             "video": "",
#             "quiz": {
#                 "title": f"shortcode - {line.replace('[Topic]', '').strip()}",
#                 "id": ""
#             }
#         }
#         if current_lesson:
#             current_lesson["topics"].append(topic)

# # Thêm lesson cuối cùng nếu có
# if current_lesson:
#     data["lessons"].append(current_lesson)

# # Xuất ra file JSON
# with open('muc_luc.json', 'w', encoding='utf-8') as json_file:
#     json.dump(data, json_file, ensure_ascii=False, indent=4)

# print("Đã chuyển đổi thành công sang file muc_luc.json")

import json

# Khởi tạo cấu trúc dữ liệu
data = {
    "title": "",
    "id": "",
    "lessons": []
}

# Đọc nội dung từ file muc_luc.txt
with open('muc_luc.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

current_lesson = None

for line in lines:
    line = line.strip()
    if line.startswith("[Course]"):
        data["title"] = line.replace("[Course]", "").strip()  # Lấy tiêu đề khóa học
    elif line.startswith("[Lesson]"):
        if current_lesson:
            data["lessons"].append(current_lesson)
        current_lesson = {
            "title": line.replace("[Lesson]", "").strip(),
            "id": "",
            "topics": []
        }
    elif line.startswith("[Topic]"):
        topic_title = line.replace("[Topic]", "").strip()
        # Thay thế các dấu nháy kép kiểu “ và ” bằng dấu nháy kép chuẩn
        topic_title = topic_title.replace('“', '"').replace('”', '"')
        # Escape các dấu nháy kép
        topic_title = topic_title.replace('"', '\"')  
        
        topic = {
            "title": topic_title,
            "topic_id": "",
            "video": "",
            "quiz": {
                "title": f"shortcode - {topic_title}",
                "id": ""
            }
        }
        if current_lesson:
            current_lesson["topics"].append(topic)

# Thêm lesson cuối cùng nếu có
if current_lesson:
    data["lessons"].append(current_lesson)

# Xuất ra file JSON
with open('muc_luc.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Đã chuyển đổi thành công sang file muc_luc.json")