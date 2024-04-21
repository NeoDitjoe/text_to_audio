import pyttsx3
from PyPDF2 import PdfReader

reader = PdfReader(open("Kagiso_Ditjoe.pdf", 'rb'))
clean_text = ''

for page_num in range(len(reader.pages)):
    text = reader.pages[page_num]
    get_text = text.extract_text()
    clean_text += get_text.strip().replace('\n', ' ')

engine = pyttsx3.init()
engine.save_to_file(clean_text, 'audio.mp3')
engine.runAndWait()
engine.stop()
