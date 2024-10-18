import os
from moviepy.editor import *

def list_mp4_files():
    # Lấy danh sách tất cả các file .mp4 trong thư mục hiện tại
    files = [f for f in os.listdir() if f.endswith('.mp4')]
    return files

def convert_mp4_to_mp3(mp4_file, mp3_file):
    # Đọc file video MP4
    video = VideoFileClip(mp4_file)
    
    # Trích xuất phần âm thanh từ video
    audio = video.audio
    
    # Lưu âm thanh dưới dạng file MP3
    audio.write_audiofile(mp3_file)

def main():
    print("Tìm các file MP4 trong thư mục hiện tại...\n")
    
    mp4_files = list_mp4_files()

    # Hiển thị danh sách file MP4 cho người dùng
    if not mp4_files:
        print("Không tìm thấy file MP4 nào trong thư mục.")
        return
    
    for idx, file in enumerate(mp4_files, start=1):
        print(f"{idx}. {file}")

    # Người dùng chọn file theo số thứ tự
    choice = int(input("\nNhập số thứ tự của file MP4 bạn muốn chuyển đổi: ")) - 1
    
    if choice < 0 or choice >= len(mp4_files):
        print("Số không hợp lệ.")
        return

    mp4_file = mp4_files[choice]
    mp3_file = mp4_file.replace(".mp4", ".mp3")
    
    print(f"\nĐang chuyển đổi '{mp4_file}' sang '{mp3_file}'...")
    
    convert_mp4_to_mp3(mp4_file, mp3_file)

    print(f"Hoàn thành! File MP3 đã được lưu thành '{mp3_file}'.")

if __name__ == "__main__":
    main()
