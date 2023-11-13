import pyaudio
import wave
from pydub import AudioSegment

# Define the input MP3 file and output WAV file
input_mp3_file = "wolf.mp3"
output_wav_file = "temp_audio.wav"
output_final_file = "special_voice.wav"

# Extract the portion from the beginning up to the 4th second
start_time_seconds = 0
end_time_seconds = 4

# Convert MP3 to WAV using pydub
audio = AudioSegment.from_mp3(input_mp3_file)
audio.export(output_wav_file, format="wav")

# Open the converted WAV file
audio = pyaudio.PyAudio()
wf = wave.open(output_final_file, 'wb')

# Set the parameters for the WAV file
wf.setnchannels(1)
wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
wf.setframerate(44100)

# Read and write audio data
chunk = 1024
start_frame = int(start_time_seconds * 44100)
end_frame = int(end_time_seconds * 44100)
frames = []

with wave.open(output_wav_file, 'rb') as wavfile:
    wavfile.setpos(start_frame)
    frames = wavfile.readframes(end_frame - start_frame)

wf.writeframes(b''.join(frames))

# Close the audio stream and WAV file
wf.close()
audio.terminate()

print(f"Extracted audio saved as '{output_final_file}'")
