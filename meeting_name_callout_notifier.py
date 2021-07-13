# Program to make a simple
# login screen


import tkinter as tk
import pyaudio
import wave
import speech_recognition as sr
import os
from twilio.rest import Client



def record():
  CHUNK = 1024
  FORMAT = pyaudio.paInt16
  CHANNELS = 2
  RATE = 44100
  RECORD_SECONDS = 10
  global WAVE_OUTPUT_FILENAME
  WAVE_OUTPUT_FILENAME="audio.wav"
  p = pyaudio.PyAudio()

  stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
              input=True,
                frames_per_buffer=CHUNK)

  print("* Starting recording")

  frames = []

  for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
      data = stream.read(CHUNK)
      frames.append(data)

  print("* Done recording")

  stream.stop_stream()
  stream.close()
  p.terminate()

  wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
  wf.setnchannels(CHANNELS)
  wf.setsampwidth(p.get_sample_size(FORMAT))
  wf.setframerate(RATE)
  wf.writeframes(b''.join(frames))
  wf.close()
  

def trans(name,sid,auth,mob,twiliono):
  filename = WAVE_OUTPUT_FILENAME
  r = sr.Recognizer()
  with sr.AudioFile(filename) as source:
      audio_data = r.record(source)
      text = r.recognize_google(audio_data,language="en-IN",show_all=True)
  if len(text)==0:
        
        pass
  else:
        
        a=(text.get("alternative")[0]).get("transcript")
        lowername=str(name)
        
        
        if (lowername.lower() in a) or (lowername.title()in a ) or (lowername.upper() in a):
              
              send_sms(name,sid,auth,mob,twiliono)
              
        else:
              pass
def send_sms(name,sid,auth,mob,twiliono):
      
  
 

#name the following line needs your Twilio Account SID and Auth Token
 l=name
 client = Client(sid,auth)

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with

 client.messages.create(to=mob, 
                       from_=twiliono, 
                       body="Your name has been called.Please respond")            
            
def loopit(name,sid,auth,mob,twiliono):       
   
 while(1):
  record()
  trans(name,sid,auth,mob,twiliono)
 
root=tk.Tk()

# setting the windows size
root.title("Called_you")
#FIXED SIZE OF WINDOW
root.minsize(400,200)
root.maxsize(400,200)
HEIGHT = 300
WIDTH = 300

# declaring string variable
# for storing name and password
name_var=tk.StringVar()
sid_var=tk.StringVar()
auth_var=tk.StringVar()
mob_var=tk.StringVar()
twiliono_var=tk.StringVar()

# defining a function that will
# get the name and password and
# print them on the screen
def submit():
 if(name_var.get()):
     
  name=name_var.get()
 else:
     name="d"
 if(sid_var.get()):
     
  sid=sid_var.get()
 else:
     name="e"
 if(auth_var.get()):
     
  auth=auth_var.get()
 else:
     name="f" 
 if(mob_var.get()):
     
  mob=mob_var.get()
 else:
     name="g" 
 if(twiliono_var.get()):
     
  twiliono=twiliono_var.get()
 else:
     name="h"   
 name=name_var.get()
 sid=sid_var.get()
 auth=auth_var.get()
 mob=mob_var.get()
 twiliono=twiliono_var.get()     
 
 
 
 loopit(name,sid,auth,mob,twiliono)
	
	
 name_var.set("")
 sid_var.set("")
 auth_var.set("")
 mob_var.set("")
 twiliono_var.set("")
	
name_label = tk.Label(root, text = 'Enter the name', font=('calibre',10, 'bold'))
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))


sid_label = tk.Label(root, text = 'Enter the Twilio SID ', font = ('calibre',10,'bold'))
sid_entry=tk.Entry(root, textvariable = sid_var, font = ('calibre',10,'normal'), show = '*')

auth_label = tk.Label(root, text = 'Enter the auth token', font=('calibre',10, 'bold'))
auth_entry = tk.Entry(root,textvariable = auth_var, font=('calibre',10,'normal'))

mob_label = tk.Label(root, text = 'Enter the  mobile number', font=('calibre',10, 'bold'))
mob_entry = tk.Entry(root,textvariable = mob_var, font=('calibre',10,'normal'))

twiliono_label = tk.Label(root, text = 'Enter the twilio  mobile number', font=('calibre',10, 'bold'))
twiliono_entry = tk.Entry(root,textvariable = twiliono_var, font=('calibre',10,'normal'))

sub_btn=tk.Button(root,text = 'Submit', command = submit)
stop_btn=tk.Button(root,text = 'Stop',command= root.destroy)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)

sid_label.grid(row=1,column=0)
sid_entry.grid(row=1,column=1)

auth_label.grid(row=2,column=0)
auth_entry.grid(row=2,column=1)

mob_label.grid(row=3,column=0)
mob_entry.grid(row=3,column=1)

twiliono_label.grid(row=4,column=0)
twiliono_entry.grid(row=4,column=1)

sub_btn.grid(row=10,column=1)
stop_btn.grid(row=12,column=1)

# performing an infinite loop
# for the window to display
root.mainloop()

