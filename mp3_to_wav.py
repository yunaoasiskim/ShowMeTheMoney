from os import path
from pydub import AudioSegment
import glob
import tqdm

hiphop_mp3_files = glob.glob('./music_mp3/HIPHOP/*.mp3')
not_hiphop_mp3_files = glob.glob('./music_mp3/~HIPHOP/*.mp3')


# for hiphop_music_file_name in tqdm.tqdm(hiphop_mp3_files):
#     wav_file_name = hiphop_music_file_name.replace('mp3', 'wav')
#     sound = AudioSegment.from_mp3(hiphop_music_file_name)
#     sound.export(wav_file_name, format="wav")


for non_hiphop_music_file_name in tqdm.tqdm(not_hiphop_mp3_files):
    wav_file_name = non_hiphop_music_file_name.replace('mp3', 'wav')
    sound = AudioSegment.from_mp3(non_hiphop_music_file_name)
    sound.export(wav_file_name, format="wav")