# import os
# import json
# import re
# from unidecode import unidecode

# def update_folder_names(json_file, course_folder):
#     with open(json_file, 'r', encoding='utf-8') as file:
#         data = json.load(file)

#     log_file = os.path.join(course_folder, "update_log.txt")

#     def normalize_name(name):
#         normalized = unidecode(name)
#         normalized = re.sub(r'[^a-zA-Z0-9_()]+', '_', normalized)
#         return normalized.strip('_').lower()

#     def log_message(message):
#         print(message)
#         with open(log_file, 'a', encoding='utf-8') as log:
#             log.write(message + '\n')

#     def list_existing_folders(path):
#         return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

#     def process_topics(lesson_folder, topics):
#         existing_topics = list_existing_folders(lesson_folder)
#         print(f"Existing Topics in {lesson_folder}: {existing_topics}")

#         for topic in topics:
#             topic_name = normalize_name(topic["title"])
#             quiz_id = topic.get("quiz", {}).get("id")

#             # Tìm thư mục khớp nhất
#             matched_folder = next((f for f in existing_topics if topic_name in f), None)
#             if not matched_folder:
#                 log_message(f"❌ Topic folder not found: {topic_name}")
#                 continue

#             topic_folder = os.path.join(lesson_folder, matched_folder)
#             if not quiz_id:
#                 log_message(f"❌ Missing quiz ID for topic: {topic['title']}")
#                 continue

#             # Thư mục cần đổi tên
#             shortcode_folder = os.path.join(topic_folder, "shortcode")
#             video_folder = os.path.join(topic_folder, "video")
#             new_shortcode_folder = os.path.join(topic_folder, f"shortcode_{quiz_id}")
#             new_video_folder = os.path.join(topic_folder, f"video_{quiz_id}")

#             # Đổi tên thư mục shortcode
#             if os.path.exists(shortcode_folder):
#                 os.rename(shortcode_folder, new_shortcode_folder)
#                 log_message(f"🔄 Renamed: {shortcode_folder} -> {new_shortcode_folder}")
#             elif os.path.exists(new_shortcode_folder):
#                 log_message(f"✅ Shortcode folder already exists: {new_shortcode_folder}")
#             else:
#                 log_message(f"❌ Shortcode folder not found: {shortcode_folder}")

#             # Đổi tên thư mục video
#             if os.path.exists(video_folder):
#                 os.rename(video_folder, new_video_folder)
#                 log_message(f"🔄 Renamed: {video_folder} -> {new_video_folder}")
#             elif os.path.exists(new_video_folder):
#                 log_message(f"✅ Video folder already exists: {new_video_folder}")
#             else:
#                 log_message(f"❌ Video folder not found: {video_folder}")

#     # Xử lý từng bài học
#     for lesson in data.get("lessons", []):
#         lesson_name = normalize_name(lesson["title"])
#         lesson_folder = os.path.join(course_folder, f"lesson_{lesson_name}")
#         if os.path.exists(lesson_folder):
#             log_message(f"\n📁 Processing Lesson: {lesson_folder}")
#             process_topics(lesson_folder, lesson.get("topics", []))
#         else:
#             log_message(f"❌ Lesson folder not found: {lesson_folder}")

# # Đường dẫn
# json_file_path = "deuschfuns-course-lesson-topic-quiz-dir-structure-1_with_id.json"
# course_folder_path = "course_"

# update_folder_names(json_file_path, course_folder_path)

import os
import json
import re
from unidecode import unidecode

def update_folder_names(json_file, course_folder):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    log_file = os.path.join(course_folder, "update_log.txt")

    def normalize_name(name):
        # Chuyển tên thành không dấu và thay ký tự đặc biệt thành "_"
        normalized = unidecode(name)
        normalized = re.sub(r'[^a-zA-Z0-9_()]+', '_', normalized)
        return normalized.strip('_').lower()

    def log_message(message):
        # Ghi log thông tin xử lý
        print(message)
        with open(log_file, 'a', encoding='utf-8') as log:
            log.write(message + '\n')

    def list_existing_folders(path):
        # Lấy danh sách các thư mục con có trong một thư mục
        return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

    def process_topics(lesson_folder, topics):
        existing_topics = list_existing_folders(lesson_folder)
        print(f"Existing Topics in {lesson_folder}: {existing_topics}")

        for topic in topics:
            topic_name = normalize_name(topic["title"])
            topic_id = topic.get("topic_id")
            quiz_id = topic.get("quiz", {}).get("id")

            # Tìm thư mục khớp nhất với topic_name
            matched_folder = next((f for f in existing_topics if topic_name in f), None)
            if not matched_folder:
                log_message(f"❌ Topic folder not found: {topic_name}")
                continue

            topic_folder = os.path.join(lesson_folder, matched_folder)

            # Thư mục cần đổi tên
            shortcode_folder = os.path.join(topic_folder, "shortcode")
            video_folder = os.path.join(topic_folder, "video")
            new_shortcode_folder = os.path.join(topic_folder, f"shortcode_{quiz_id}") if quiz_id else None
            new_video_folder = os.path.join(topic_folder, f"video_{topic_id}")

            # Đổi tên thư mục shortcode nếu quiz_id tồn tại
            if quiz_id:
                if os.path.exists(shortcode_folder):
                    os.rename(shortcode_folder, new_shortcode_folder)
                    log_message(f"🔄 Renamed: {shortcode_folder} -> {new_shortcode_folder}")
                elif os.path.exists(new_shortcode_folder):
                    log_message(f"✅ Shortcode folder already exists: {new_shortcode_folder}")
                else:
                    log_message(f"❌ Shortcode folder not found: {shortcode_folder}")

            # Đổi tên thư mục video với topic_id
            if os.path.exists(video_folder):
                os.rename(video_folder, new_video_folder)
                log_message(f"🔄 Renamed: {video_folder} -> {new_video_folder}")
            elif os.path.exists(new_video_folder):
                log_message(f"✅ Video folder already exists: {new_video_folder}")
            else:
                log_message(f"❌ Video folder not found: {video_folder}")

    # Xử lý từng bài học
    for lesson in data.get("lessons", []):
        lesson_name = normalize_name(lesson["title"])
        lesson_folder = os.path.join(course_folder, f"lesson_{lesson_name}")
        if os.path.exists(lesson_folder):
            log_message(f"\n📁 Processing Lesson: {lesson_folder}")
            process_topics(lesson_folder, lesson.get("topics", []))
        else:
            log_message(f"❌ Lesson folder not found: {lesson_folder}")

# Đường dẫn
json_file_path = "muc_luc_with_id.json"
course_folder_path = "course_"

update_folder_names(json_file_path, course_folder_path)
