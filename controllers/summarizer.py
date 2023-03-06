import openai
import os                                                                                                                                                                                                          
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(Path(".env"))

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_transcript(transcript):
    prompt = "Here is the raw audio transcript from a podcast:\n" + transcript + "What are the key takeaways? Provide the outputs in markdown format using headings and bullet points."
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an expert podcast summarizer. You can take podcast transcripts, extract the most relevant information from them and tell people about the most important parts of it."},
        {"role": "user", "content": prompt}
    ]
    )
    print(response)
    summary = response.choices[0].message.content
    print(summary)
    return summary