from os import path
from pydub import AudioSegment
import glob
import tqdm
import subprocess

hiphop_mp3_files = glob.glob('./music_wav/HIPHOP/*.wav')
not_hiphop_mp3_files = glob.glob('./music_wav/~HIPHOP/*.wav')

print(hiphop_mp3_files)

for hiphop_music_file_name in tqdm.tqdm(hiphop_mp3_files):
    wav_file_name = hiphop_music_file_name.replace('wav', 'midi')
    subprocess.run(['audio-to-midi', "{}".format(hiphop_music_file_name)])