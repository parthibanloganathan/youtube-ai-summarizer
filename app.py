from flask import Flask, request, Response
import youtube_dl

app = Flask(__name__)

@app.route('/extract', methods=['POST'])
def extract():
    url = request.form['url']
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        audio_url = info_dict.get("url", None)
        if audio_url:
            response = Response()
            response.headers['Content-Type'] = 'audio/mp4'
            response.headers['Content-Disposition'] = 'attachment; filename=audio.mp4'
            response.headers['X-Accel-Redirect'] = audio_url
            return response
    return "Error: Could not extract audio from the video."
