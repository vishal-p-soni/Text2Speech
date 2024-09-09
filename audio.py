import pdfplumber as pp
from gtts import gTTS

pdf_text = ''

with pp.open('/Users/vishalsoni/Documents/AI_Projects/SpeechRecognization/Deep_C_Secrets_Expert_C_Programming.pdf') as pdf:
    for page in pdf.pages:
        pdf_text += page.extract_text()

tts = gTTS(text=pdf_text, lang='en')
tts.save('audio_book.mp3')