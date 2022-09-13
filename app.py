import speech_recognition as sr


# You can find your microphone device index via this line of code, My mic is 5th item of list. So it is index=4 
# print(sr.Microphone.list_microphone_names())

listener = sr.Recognizer()
try:
  with sr.Microphone(device_index=4) as source: # Change index with your mic index,othervise will not work.
    print('listening...')
    voice = listener.listen(source)
    command = listener.recognize_google(voice)
    print(command)

except:
  pass
