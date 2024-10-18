import yt_dlp
import os

def download_youtube_video(link):
    ydl_opts = {
        'format': 'best',  # Tải video với chất lượng tốt nhất
        'outtmpl': '%(title)s.%(ext)s'  # Đặt tên file dựa trên tiêu đề video
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Tải video thành công!")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Tool tải video YouTube")

    while True:
        link = input("Nhập link video YouTube (hoặc 'thoat' để thoát): ")
        
        if link.lower() == 'thoat':
            break
        
        download_youtube_video(link)
        input("Nhấn Enter để tiếp tục...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
