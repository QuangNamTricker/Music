import os
from pydub import AudioSegment

def list_audio_files(folder):
    """Liệt kê tất cả các file mp3, wav trong thư mục."""
    files = [f for f in os.listdir(folder) if f.endswith(('.mp3', '.wav'))]
    for idx, file in enumerate(files):
        print(f"{idx + 1}. {file}")
    return files

def merge_audio_files(folder, selected_files, output_file):
    """Gộp danh sách file đã chọn thành 1 file duy nhất."""
    merged_audio = AudioSegment.empty()

    for file in selected_files:
        file_path = os.path.join(folder, file)
        sound = AudioSegment.from_file(file_path)
        merged_audio += sound  # Nối âm thanh lại

    merged_audio.export(output_file, format=output_file.split('.')[-1])
    print(f"Xuất file thành công: {output_file}")

def main():
    folder = input("Nhập đường dẫn thư mục chứa file nhạc: ")
    if not os.path.isdir(folder):
        print("Thư mục không hợp lệ!")
        return

    files = list_audio_files(folder)

    # Nhập số thứ tự của file muốn gộp
    selections = input("Nhập số thứ tự các bài hát muốn gộp (cách nhau bởi dấu phẩy): ")
    try:
        selected_files = [files[int(idx) - 1] for idx in selections.split(",")]
    except (ValueError, IndexError):
        print("Lựa chọn không hợp lệ!")
        return

    output_format = input("Xuất file dưới định dạng nào? (mp3 hoặc wav): ").strip().lower()
    if output_format not in ["mp3", "wav"]:
        print("Định dạng không hợp lệ!")
        return

    output_file = os.path.join(folder, f"merged_output.{output_format}")
    merge_audio_files(folder, selected_files, output_file)

if __name__ == "__main__":
    main()
