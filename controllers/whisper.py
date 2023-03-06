from pytube import YouTube
from pydub import AudioSegment
import openai
import os                                                                                                                                                                                                          
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(Path(".env"))
from moviepy.editor import *

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_transcript_from_audio(filename):
    print("Chunking audio and getting transcript...")
    final_transcript = ""

    # audio_file_path = "/Users/parthi/Downloads/lex_ai_aaron_smith_levin.mp3"
    audio = AudioSegment.from_mp3(filename)
    
    # Chunk audio first
    CHUNK_LENGTH = 10 * 60 * 1000 # 10 mins
    total_segments = (len(audio) // CHUNK_LENGTH) + 1
    print(total_segments)

    for i in range(total_segments):
        print(i)
        start = i * CHUNK_LENGTH
        end = start + CHUNK_LENGTH
        segment = audio[start:end]
        file_name = f"segment_{i+1}.mp3"
        segment.export(file_name, format="mp3")
        final_transcript += get_transcript(file_name)
    
    print(final_transcript)
    file = open("transcript.txt", "w")
    file.write(final_transcript)
    file.close()
    
    return final_transcript

def get_transcript(filename):
    file = open(filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", file).text
    print(transcript)
    return transcript

def download_audio(url='https://www.youtube.com/watch?v=eKhVnsZ2xY4'):
    yt = YouTube(url)
    stream = yt.streams.get_by_itag(18)

    print('--- START: Downloading Video')
    video_filename = 'video.mp4'
    stream.download(filename=video_filename)
    print('--- END: Downloading Video')

    print('--- START: Extracting Audio')
    video_fileclip = VideoFileClip(video_filename)
    audio = video_fileclip.audio

    audio_filename = 'audio.mp3'
    audio.write_audiofile(audio_filename)
    print('--- END: Extracting Audio')

    return audio_filename

if __name__ == '__main__':
    get_transcript()
    # yt = YouTube('https://www.youtube.com/watch?v=eKhVnsZ2xY4')
    # yt.captions['a.en'].download(title='test', srt=True)
    # download_audio()
    # get_transcript_from_audio(filename)
    

