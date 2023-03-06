from pytube import YouTube
from pydub import AudioSegment
import openai
import os                                                                                                                                                                                                          
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(Path(".env"))

openai.api_key = os.getenv("OPENAI_API_KEY")

audio_file_path = # parth here to file
audio_file= open(audio_file_path, "rb")

# audio = AudioSegment.from_mp3(audio_file_path)

# def chunk_audio():
#     CHUNK_LENGTH = 10 * 60 * 1000 # 10 mins
#     total_segments = (len(audio) // CHUNK_LENGTH) + 1

#     for i in range(total_segments):
#         print(i)
#         start = i * CHUNK_LENGTH
#         end = start + CHUNK_LENGTH
#         segment = audio[start:end]
#         segment.export(f"segment_{i+1}.mp3", format="mp3")

def get_transcript():
    print("Opening file", audio_file)
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print('--- transcript', transcript)

if __name__ == '__main__':
    get_transcript()
    # yt = YouTube('https://www.youtube.com/watch?v=eKhVnsZ2xY4')
    # yt.captions['a.en'].download(title='test', srt=True)
    # chunk_audio()
    

