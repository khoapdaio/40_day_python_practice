#Day 29

# !pip install librosa
# !pip install SpeechRecognition
# !pip install gtts
#
# !pip install pydub

# Sử dụng thư viện librosa để visualize âm thanh

import librosa
import numpy as np
import matplotlib.pyplot as plt

filename ='/content/drive/MyDrive/Colab Notebooks/file-music.mp3'


audio,sr =librosa.load(filename)

time = np.linspace(0,audio.shape[0]/sr,num=audio.shape[0])
plt.plot(time, audio,color="blue")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (quantized)")
plt.title("Wav file visualization")
plt.axhline(y=0,color='r',linestyle='-')
plt.show()




import speech_recognition as sr
from pydub import AudioSegment


filename ='/content/drive/MyDrive/Colab Notebooks/file-music.mp3'
r= sr.Recognizer()

my_audio = AudioSegment.from_mp3(filename)
my_audio.export("/content/drive/MyDrive/Colab Notebooks/recording.wav", format="wav")

temp = '/content/drive/MyDrive/Colab Notebooks/recording.wav'

my_audio = sr.AudioFile(temp)
with my_audio as source:
  audio = r.record(source,duration=200)


print( f"- Type: {type(audio)}")

your_speech = r.recognize_google(audio, language="vi-VN")

print(f"Audio transcription: {your_speech}")

from gtts import gTTS
import librosa
import numpy as np
import IPython

lang = 'vi'
filename ='/content/drive/MyDrive/Colab Notebooks/file-music.mp3'

data , sr = librosa . load ( filename )
IPython . display . display ( IPython . display . Audio ( np . transpose ( data ) ,
rate = sr ) )
