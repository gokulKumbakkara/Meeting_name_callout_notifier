# 🎙️ Called_You — Meeting name callout notifier  

This project implements a **Tkinter-based desktop application** that records audio, transcribes it using **Google Speech Recognition**, and checks if a specified **name** was called. If detected, it sends an **SMS alert via Twilio** to a configured mobile number.  

---

## 📌 Features
- 🎤 Records 10-second audio samples continuously  
- 📝 Uses **SpeechRecognition (Google API)** for transcription  
- 🔍 Detects if the specified **name** is mentioned in speech  
- 📲 Sends SMS notification via **Twilio API**  
- 🖥️ Simple Tkinter-based GUI for entering credentials and details  

---

## 📦 Packages Used
- **tkinter** → GUI for input fields and buttons  
- **pyaudio** → Recording audio from microphone  
- **wave** → Saving audio recordings in `.wav` format  
- **speechrecognition** → Google API-based speech-to-text transcription  
- **os** → File handling and process utilities  
- **twilio** → Sending SMS alerts through Twilio API  
