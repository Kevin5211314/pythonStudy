
#!/usr/bin/python3
# -*- coding: UTF-8 -*-s

import wave
import pyaudio

CHUNK = 1024

music_path = '二珂-突然之间.wav'

wf = wave.open(music_path, 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()

p.terminate()