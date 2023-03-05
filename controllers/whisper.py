import openai

def get_transcript(audio):
    audio_file= open("/path/to/file/audio.mp3", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
