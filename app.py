from flask import Flask, request, Response
from pytube import YouTube
from controllers.summarizer import summarize_transcript
from controllers.whisper import download_audio, get_transcript_from_audio

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def extract():
    print("/summarize")
    url = request.args.get("url")
    print(url)
    # audio_filename = download_audio(url)
    # transcript = get_transcript_from_audio(audio_filename)
    # transcript = get_transcript_from_audio("audio.mp3")

    with open("transcript.txt", "r") as f:
        # Read the contents of the file into a string variable
        transcript = f.read()

    return summarize_transcript(transcript)

@app.route('/sum', methods=['GET'])
def sum():
    return summarize_transcript()
    
@app.get("/")
def home():
    return "Flask is running"

if __name__ == "__main__":
    app.run(debug=True)