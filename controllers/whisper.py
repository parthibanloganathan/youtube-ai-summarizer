import openai
from pytube import YouTube
import os

def get_transcript():
    audio_file= open("/Users/rraina/Documents/pet_projects/chatgpt-hackathon/youtube-ai-summarizer/audio-samples/lex_ai_aaron_smith_levin_short.mp3", "rb")
    print("Opening file", audio_file)
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print('--- transcript', transcript)

if __name__ == '__main__':
    # get_transcript()
    yt = YouTube('https://www.youtube.com/watch?v=eKhVnsZ2xY4')
    yt.captions['a.en'].download(title='test', srt=False)
    

