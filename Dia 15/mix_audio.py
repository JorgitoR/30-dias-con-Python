import os
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from moviepy.audio.fx.all import volumex
from PIL import Image
from moviepy.video.fx.all  import crop


source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
source_audio_path = os.path.join(SAMPLE_INPUTS, 'audio.mp3')
audio_dir = os.path.join(SAMPLE_OUTPUTS, "audio")
os.makedirs(audio_dir, exist_ok=True)

og_audio_ruta = os.path.join(audio_dir, 'og.mp3')
audio_final_ruta = os.path.join(audio_dir, 'final.mp3')
video_final_ruta = os.path.join(audio_dir, 'video_final.mp4')

video_clip = VideoFileClip(source_path)
audio_original = video_clip.audio 
audio_original.write_audiofile(og_audio_ruta)


background_audio_clip = AudioFileClip(source_audio_path)
bg_music = background_audio_clip.subclip(0, video_clip.duration)

#bg_music = bg_music.fx(volumex, 0.10)
bg_music = bg_music.volumex(0.10)

audio_final = CompositeAudioClip([audio_original, bg_music])
audio_final.write_audiofile(audio_final_ruta, fps=audio_original.fps)

final_clip = video_clip.set_audio(audio_final)
final_clip.write_audiofile(video_final_ruta, codec='libx264', audio_codec="aac")

