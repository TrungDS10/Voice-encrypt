# Import necessery module 
from tkinter import *
from PIL import ImageTk, Image 
import speech_recognition as sr
import pyttsx3

# Create object for text-to-speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Creating root object 
root = Tk() 

# Defining size of window 
root.geometry("1400x600") 

# Add image file
bg = PhotoImage(file= 'ava.png')
bg1 = ImageTk.PhotoImage(Image.open('Vigenere.jpg'))

# Show image using label
ava = Label(root, image= bg)
ava.place(x= 0, y= 0)

ava1 = Label(root, image= bg1)
ava1.place(x= 950, y= 0)

# Setting up the title of window 
root.title('Voice Encryption and Decryption') 

Tops = Frame(root, width= 1600, relief= SUNKEN) 
Tops.pack(side= TOP) 

f1 = Frame(root, width= 800, height= 700, relief= SUNKEN) 
f1.pack(side= LEFT) 

# Header
lblInfo = Label(Tops, font= ('helvetica', 50, 'bold'), text= 'SECRET MESSAGING \n VIGENÈRE CIPHER', 
				fg= "Black", bd= 10, anchor= 'w') 
                    
lblInfo.grid(row= 0, column= 0) 
 
Msg = StringVar() 
key = StringVar() 
mode = StringVar() 
Result = StringVar() 

# Exit function 
def qExit(): 
    root.destroy() 

# Function to reset the window 
def Reset(): 
    Msg.set('') 
    key.set('') 
    mode.set('') 
    Result.set('') 

# Speak recognizer function
def Speak():
    r = sr.Recognizer()
    r.pause_threshold = 0.7
    r.energy_threshold = 400

    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=5)
            Msg = str(r.recognize_google(audio))
            txtMsg.focus()
            txtMsg.delete(0, END)
            txtMsg.insert(0, Msg)

        except sr.UnknownValueError:
            print('Google Speech Recognition could not understand audio')

        except sr.RequestError as e:
            print('Could not request results from Google Speech Recognition Service')

        else:
            pass

def Speak1():
    r = sr.Recognizer()
    r.pause_threshold = 0.7
    r.energy_threshold = 400

    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=5)
            key = str(r.recognize_google(audio))
            txtkey.focus()
            txtkey.delete(0, END)
            txtkey.insert(0, key)

        except sr.UnknownValueError:
            print('Google Speech Recognition could not understand audio')

        except sr.RequestError as e:
            print('Could not request results from Google Speech Recognition Service')

        else:
            pass
        
# Labels and their position
lblMsg = Label(f1, font= ('arial', 16, 'bold'), text= 'YOUR MESSAGE', bd= 16, anchor= 'w') 
lblMsg.grid(row= 0, column= 3) 

txtMsg = Entry(f1, font= ('arial', 16, 'bold'), textvariable= Msg, bd= 10, insertwidth= 4, 
				bg= 'powder blue', justify = 'right', width= 35) 
txtMsg.grid(row= 0, column= 6) 

lblkey = Label(f1, font= ('arial', 16, 'bold'), text= 'YOUR KEY', bd= 16, anchor= 'w')             
lblkey.grid(row= 1, column= 3) 

txtkey = Entry(f1, font= ('arial', 16, 'bold'), textvariable= key, bd= 10, insertwidth= 4, 
				bg= 'powder blue', justify= 'right', width= 35)                 
txtkey.grid(row= 1, column= 6) 

lblmode = Label(f1, font= ('arial', 16, 'bold'), text= 'ENCRYPT(E)/DECRYPT(D)', bd= 16, anchor= 'w')                                 
lblmode.grid(row= 2, column= 3) 

txtmode = Entry(f1, font= ('arial', 16, 'bold'), textvariable= mode, bd= 10, insertwidth= 4, 
				bg= 'powder blue', justify= 'right', width= 35)                     
txtmode.grid(row= 2, column= 6) 

lblService = Label(f1, font= ('arial', 16, 'bold'), text= 'RESULT', bd= 16, anchor= 'w')             
lblService.grid(row= 3, column= 3) 

txtService = Entry(f1, font= ('arial', 16, 'bold'), textvariable= Result, bd= 10, insertwidth= 4, 
					bg= 'powder blue', justify= 'right', width= 35)                         
txtService.grid(row= 3, column= 6) 

# Speak buttons
btnSpeak = Button(f1, padx= 4, pady= 2, bd= 4, fg= 'black', font= ('arial', 16, 'bold'), width= 10, 
					text= 'Speak', bg= 'blue', command= Speak).grid(row= 0, column= 10) 

btnSpeak1 = Button(f1, padx= 4, pady= 2, bd= 4, fg= 'black', font= ('arial', 16, 'bold'), width= 10, 
					text= 'Speak', bg= 'blue', command= Speak1).grid(row= 1, column= 10) 

# Vigenère cipher 
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Encode and decode message
def encode(key, Msg):
    return translateMessage(key, Msg, 'encrypt')
def decode(key, Msg):
    return translateMessage(key, Msg, 'decrypt')

def translateMessage(key, Msg, mode):
    translated = [] 
    keyIndex = 0
    key = key.upper()
    for symbol in Msg:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])
            num %= len(LETTERS)
                
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            keyIndex += 1
                
            if keyIndex == len(key):
                 keyIndex = 0
        else:
            translated.append(symbol)
    return ''.join(translated)

# Show result    
def Ref(): 
    if (mode.get() == 'e'): 
        Result.set(encode(key.get(), Msg.get())) 
    else: 
        Result.set(decode(key.get(), Msg.get()))         

def say():
    engine.say(decode(key.get(), Msg.get()))
    engine.runAndWait()
    engine.stop()

# Show message button 
btnTotal = Button(f1, padx= 16, pady= 8, bd= 16, fg= 'black', font= ('arial', 16, 'bold'), width= 10, 
					text= 'Show Message', bg= 'powder blue', command= Ref).grid(row= 7, column= 4) 

# Reset button 
btnReset = Button(f1, padx= 16, pady= 8, bd= 16, fg= 'black', font= ('arial', 16, 'bold'), width= 10, 
					text= 'Reset', bg= 'green', command= Reset).grid(row= 7, column= 6) 

# Exit button 
btnExit = Button(f1, padx= 16, pady= 8, bd= 16, fg= 'black', font= ('arial', 16, 'bold'), width= 10, 
					text= 'Exit', bg= 'red', command= qExit).grid(row= 7, column= 8)

btnSay = Button(f1, padx= 4, pady= 2, bd= 4, fg= 'black', font= ('arial', 16, 'bold'), width= 10, 
					text= 'Read', bg= 'blue', command= say).grid(row= 3, column= 10) 

# Keeps window alive 
root.mainloop()