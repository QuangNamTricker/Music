import os
from moviepy.editor import VideoFileClip, AudioFileClip

def cut_video(input_file, output_file, start_time, duration):
    with VideoFileClip(input_file) as video:
        # Cắt video từ start_time và kéo dài trong duration giây
        video = video.subclip(start_time, start_time + duration)
        video.write_videofile(output_file)

def cut_audio(input_file, output_file, start_time, duration):
    with AudioFileClip(input_file) as audio:
        # Cắt audio từ start_time và kéo dài trong duration giây
        audio = audio.subclip(start_time, start_time + duration)
        audio.write_audiofile(output_file)

def main():
    current_directory = os.getcwd()  # Lấy đường dẫn thư mục hiện tại
    print(f"Thư mục hiện tại: {current_directory}")
    
    file_type = input("Nhập loại tệp (video/audio): ").strip().lower()
    
    # Hiển thị danh sách tệp trong thư mục hiện tại
    print("Danh sách các tệp trong thư mục:")
    files = [f for f in os.listdir(current_directory) if f.endswith(('.mp4', '.mp3'))]
    for idx, file in enumerate(files):
        print(f"{idx + 1}. {file}")

    # Nhập số thứ tự để chọn tệp
    file_index = int(input("Nhập số thứ tự tệp bạn muốn cắt: ")) - 1
    input_file = os.path.join(current_directory, files[file_index])
    
    start_time = int(input("Nhập thời gian bắt đầu (giây): "))
    duration = int(input("Nhập độ dài (giây): "))
    
    output_file = input("Nhập đường dẫn tệp đầu ra (vd: output.mp4 hoặc output.mp3): ")
    
    if file_type == "video":
        cut_video(input_file, output_file, start_time, duration)
    elif file_type == "audio":
        cut_audio(input_file, output_file, start_time, duration)
    else:
        print("Loại tệp không hợp lệ. Vui lòng nhập 'video' hoặc 'audio'.")

if __name__ == "__main__":
    main()
