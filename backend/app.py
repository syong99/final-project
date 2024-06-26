import whisper
import yt_dlp
import os

def download_youtube_audio(url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(url, download=True)
            audio_file = ydl.prepare_filename(info_dict).replace('.webm', '.mp3').replace('.m4a', '.mp3')
            if os.path.exists(audio_file):
                return audio_file
            else:
                print(f"Expected audio file {audio_file} not found.")
                return None
        except Exception as e:
            print(f"Error downloading audio: {str(e)}")
            return None

def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]

def main():
    youtube_url = "https://www.youtube.com/watch?v=sVTy_wmn5SU"  # 원하는 유튜브 URL로 변경하세요
    output_path = "audio.mp3"

    print("Downloading YouTube audio...")
    audio_file = download_youtube_audio(youtube_url, output_path)
    
    if audio_file and os.path.exists(audio_file):
        print("Transcribing audio...")
        transcription = transcribe_audio(audio_file)
        
        print("\nTranscription:")
        print(transcription)
        
        # 오디오 파일 삭제 (선택사항)
        os.remove(audio_file)
    else:
        print("Failed to download audio.")

if __name__ == "__main__":
    main()