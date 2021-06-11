from gtts import gTTS
import playsound

text = "For this option! One pronunciation will be called." \
       "Try to guess its correct alphabet." \
       "To move to the next! press next arrow key." \
       "To hear how it's pronounced! press space key." \
       "To see its correct alphabet! press TAB."

myObj = gTTS(lang='en', slow=False, text=text)
myObj.save('opt_02.mp3')
playsound.playsound('opt_02.mp3')