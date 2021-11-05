# Import necessery module 
from tkinter import *
from PIL import ImageTk, Image 
import pyttsx3
import speech_recognition as sr

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

# Method to cover text to speech
friday = pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice', voice[0].id)

# Speak recognizer function
def Speak():
    r = sr.Recognizer()
    m = sr.Microphone()
     
    friday.say("A moment of silence, please...")
    friday.runAndWait()
    with m as source: 
        r.adjust_for_ambient_noise(source)
    
    while True:
        friday.say("Please tell me your message!")
        friday.runAndWait()
        with m as source: 
            audio = r.listen(source)
        friday.say("Got it! Now to recognize it...")
        friday.runAndWait()
        try:
            value = r.recognize_google(audio)
            print("The message you said: {}".format(value))
        except sr.UnknownValueError:
            friday.say("Oops! Didn't catch that")
            friday.runAndWait()
        except sr.RequestError as e:
            friday.say("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            friday.runAndWait()
        if value != "":
            break
    Msg.set(format(value))

def Speak1():
    r = sr.Recognizer()
    m = sr.Microphone()
    
    try:
        friday.say("A moment of silence, please...")
        friday.runAndWait()
        with m as source: r.adjust_for_ambient_noise(source)
       
        while True:
            friday.say("Please tell me your password!")
            friday.runAndWait()
            with m as source: audio1 = r.listen(source)
            friday.say("Got it! Now to recognize it...")
            try:
                value1 = r.recognize_google(audio1)
                print("The password you said: {}".format(value1))
            except sr.UnknownValueError:
                friday.say("Oops! Didn't catch that")
                friday.runAndWait()
            except sr.RequestError as e:
                friday.say("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
                friday.runAndWait()
            if value1 != "":
                break
    except KeyboardInterrupt:
        pass
    return format(value1)

# Labels and their position
lblMsg = Label(f1, font= ('arial', 16, 'bold'), text= 'YOUR MESSAGE', bd= 16, anchor= 'w') 
lblMsg.grid(row= 0, column= 3) 

txtMsg = Entry(f1, font= ('arial', 16, 'bold'), textvariable= Msg, bd= 10, insertwidth= 4, 
				bg= 'powder blue', justify = 'right') 
txtMsg.grid(row= 0, column= 6) 

lblkey = Label(f1, font= ('arial', 16, 'bold'), text= 'YOUR KEY', bd= 16, anchor= 'w')             
lblkey.grid(row= 1, column= 3) 

txtkey = Entry(f1, font= ('arial', 16, 'bold'), textvariable= key, bd= 10, insertwidth= 4, 
				bg= 'powder blue', justify= 'right')                 
txtkey.grid(row= 1, column= 6) 

lblmode = Label(f1, font= ('arial', 16, 'bold'), text= 'ENCRYPT(E)/DECRYPT(D)', bd= 16, anchor= 'w')                                 
lblmode.grid(row= 2, column= 3) 

txtmode = Entry(f1, font= ('arial', 16, 'bold'), textvariable= mode, bd= 10, insertwidth= 4, 
				bg= 'powder blue', justify= 'right')                     
txtmode.grid(row= 2, column= 6) 

lblService = Label(f1, font= ('arial', 16, 'bold'), text= 'RESULT', bd= 16, anchor= 'w')             
lblService.grid(row= 3, column= 3) 

txtService = Entry(f1, font= ('arial', 16, 'bold'), textvariable= Result, bd= 10, insertwidth= 4, 
					bg= 'powder blue', justify= 'right')                         
txtService.grid(row= 3, column= 6) 

# Speak buttons
btnSpeak = Button(f1, padx= 4, pady= 2, bd= 4, fg= 'black', font= ('arial', 16, 'bold'), width= 10, 
					text= 'Speak', bg= 'blue', command= Speak).grid(row= 0, column= 10) 

btnSpeak1 = Button(f1, padx= 4, pady= 2, bd= 4, fg= 'black', font= ('arial', 16, 'bold'), width= 10, 
					text= 'Speak', bg= 'blue', command= Speak1).grid(row= 1, column= 10) 

# Vigenère cipher
import base64 

# Function to encode 
def encode(key, clear): 
    enc = [] 
    
    for i in range(len(clear)): 
        key_c = key[i % len(key)] 
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)                   
        enc.append(enc_c) 
        
    return base64.urlsafe_b64encode(''.join(enc).encode()).decode() 

# Function to decode 
def decode(key, enc): 
    dec = [] 
    
    enc = base64.urlsafe_b64decode(enc).decode() 
    for i in range(len(enc)): 
        key_c = key[i % len(key)] 
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)                             
        dec.append(dec_c) 
    return ''.join(dec)

def Ref(): 
    clear = Msg.get() 
    k = key.get() 
    m = mode.get() 

    if (m == 'e'): 
        Result.set(encode(k, clear)) 
    else: 
        Result.set(decode(k, clear))         

# Show message button 
btnTotal = Button(f1, padx= 16, pady= 8, bd= 16, fg= 'black', font= ('arial', 16, 'bold'), width= 10, 
					text= 'Show Message', bg= 'powder blue', command= Ref).grid(row= 7, column= 4) 

# Reset button 
btnReset = Button(f1, padx= 16, pady= 8, bd= 16, fg= 'black', font= ('arial', 16, 'bold'), width= 10, 
					text= 'Reset', bg= 'green', command= Reset).grid(row= 7, column= 6) 

# Exit button 
btnExit = Button(f1, padx= 16, pady= 8, bd= 16, fg= 'black', font= ('arial', 16, 'bold'), width= 10, 
					text= 'Exit', bg= 'red', command= qExit).grid(row= 7, column= 8)

# Keeps window alive 
root.mainloop()