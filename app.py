from flask import Flask, request, Response
from pytube import YouTube
from controllers.summarizer import summarize_transcript

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def extract():
    print("/summarize")
    url = request.args.get("url")
    print(url)
    # options = {
    #     'format': 'bestaudio',
    #     'postprocessors': [{
    #         'key': 'FFmpegExtractAudio',
    #         'preferredcodec': 'mp3'
    #     }],
    # }

    # audio_downloader = YoutubeDL(options)
    # audio_downloader.extract_info(url, download=False)
    # print(audio_downloader)

    return 200

@app.route('/sum', methods=['GET'])
def sum():
    return summarize_transcript()
    
@app.get("/")
def home():
    return "Flask is running"

if __name__ == "__main__":
    app.run(debug=True)