import pyttsx3
import PyPDF2

book = open('harrypotter4.pdf','rb')
pdfreader = PyPDF2.PdfReader(book)
pg = len(pdfreader.pages)
print(pg)
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',150)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
print(rate)
engine.say('Welcome to hexcent audiobook')
for num in range(16,pg):
    page = pdfreader.pages[16]
    text = page.extract_text()
    engine.say(text)
    engine.runAndWait()