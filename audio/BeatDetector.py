from __future__ import print_function
import numpy as np
import pyaudio
import wave
import sys
import librosa

CHUNK = 1024

wf = wave.open("../songs/test.wav",'rb')
print(type(wf))
p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)
    y, sr = librosa.load(data)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    
    print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

    # 4. Convert the frame indices of beat events into timestamps
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)


stream.stop_stream()
stream.close()

p.terminate()

# Beat tracking example



# 2. Load the audio as a wavefo

# 3. Run the default beat tracker


class BeatDetector:
    def __init__(self, src, stateMachine):
        self.src = src
        self.stateMachine = stateMachine

    def detect(src):
        self.src = src
        samplerate = 0  # use original source samplerate
        hop_size = 256  # number of frames to read in one block
        total_frames = 0

        while True:
            samples, read = self.src()  # read hop_size new samples from source
            total_frames += read   # increment total number of frames
            if read < hop_size:    # end of file reached
                break

        fmt_string = "read {:d} frames at {:d}Hz from {:s}"
        print(fmt_string.format(total_frames, src.samplerate, src.uri))