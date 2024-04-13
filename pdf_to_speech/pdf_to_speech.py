'''import pyttsx3

engine=pyttsx3.init()
voices = engine.getProperty('rate')
print(voices)
engine.setProperty('rate',175)
engine.say("hi mayank aap kaise ho")
engine.runAndWait() '''



import pyttsx3,PyPDF2

#insert name of your pdf 
pdfreader = PyPDF2.PdfFileReader(open('a.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
