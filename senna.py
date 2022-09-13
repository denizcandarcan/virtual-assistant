import speech_recognition as sr
import pyttsx3
import myconfig
import pyjokes
import datetime

#? You can find your microphone device index via this line of code, My mic is 5th item of list. So it is index=4 
#? print(sr.Microphone.list_microphone_names())


#* Male voice id 0 , female voice 1
#* voices = engine.getProperty('voices')
#* engine.setProperty('voice',voices[1].id)

name=myconfig.NAME
status = True

class Senna:
  name=None
  status = True
  listener = sr.Recognizer()
  engine = pyttsx3.init()
  def __init__(self):
    self.name= myconfig.NAME
    self.engine =pyttsx3.init()
    self.listener = sr.Recognizer()

  def start(self):
    self.run()
  
  def run(self):
    while True:
      self.call(self.name)
      

  def call(self,name):
    try:
      with sr.Microphone(device_index=4) as source: # Change index with your mic index,othervise will not work.
        print('listening...')
        voice = self.listener.listen(source)
        command = self.listener.recognize_google(voice)
        command = command.lower()
        if 'senna' or 'sena' or 'senaa' or 'senasu' in command:
          self.engine.say(f'Hi my name is {name} How can i help you?')
          self.engine.runAndWait()
          self.listen()
          print(command)
        elif 'alexa' in command:
          self.engine.say('Who the fuck is Alexa?')
          self.engine.runAndWait()
        else:
          pass
    except:
      pass
  def listen(self):
      with sr.Microphone(device_index=4) as source:
        print('waiting for command')
        voice = self.listener.listen(source)
        command = self.listener.recognize_google(voice)
        command = command.lower()
        self.apply_command(command)
  
  def apply_command(self,command):
      if 'joke' in command:
          self.engine.say(pyjokes.get_joke())
          self.engine.runAndWait()
          return
      elif 'what' and 'time' in command:
        print('burada failliyor?')
        time = datetime.datetime.now().strftime('%I,%M %p')
        self.engine.say(f'Current time in your current location is:{time}')
        self.engine.runAndWait()
        return
      else:
          self.engine.say("I did not programmed for this command yet Call me back")
          self.engine.runAndWait()
          return
