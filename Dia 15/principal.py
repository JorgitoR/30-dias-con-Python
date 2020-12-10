import os
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails')
thumbnail_per_frame = os.path.join(SAMPLE_OUTPUTS, 'thumbnails_per_frame')
thumbnails_per_medio_segundo = os.path.join(SAMPLE_OUTPUTS, 'thumbnails_per_medio_segundo')

os.makedirs(thumbnail_dir, exist_ok=True)
os.makedirs(thumbnail_per_frame, exist_ok=True)
os.makedirs(thumbnails_per_medio_segundo, exist_ok=True)

clip = VideoFileClip(source_path)
print(clip.reader.fps) # frames per second
print(clip.reader.nframes)
print(clip.duration) # Segundos

duracion = clip.duration # clip.reader.duration
max_duracion = int(duracion) + 1
for i in range(0, max_duracion):
    frame = clip.get_frame(int(i))
    #print(frame) #np.array
    # Nos imprime todos los datos en Array numpy, esto actualmente
    # nos devuelve los valores del color por cada pixel individual 
    # Una imagen puede tener miles de pixeles
    nueva_img_filepath = os.path.join(thumbnail_dir, f"{i}.jpg")
    print(f"frame at {i} segundos, guardado en {nueva_img_filepath}")
    nueva_img = Image.fromarray(frame)
    nueva_img.save(nueva_img_filepath)

fps     = clip.reader.fps 
nframes = clip.reader.nframes
segundos= nframes / (fps * 1.0)

for i, frame in enumerate(clip.iter_frames()):
    if i % fps == 0:
        current_ms =int((i /fps) * 1000 )
        nueva_img_filepath = os.path.join(thumbnail_per_frame, f"{i}.jpg")
        nueva_img = Image.fromarray(frame)
        nueva_img.save(nueva_img_filepath)



for i, frame in enumerate(clip.iter_frames()):
    fphs = int(fps/2.0)
    if i % fps == 0:
        current_ms =int((i /fps) * 1000) 
        nueva_img_filepath = os.path.join(thumbnails_per_medio_segundo, f"{i}.jpg")
        nueva_img = Image.fromarray(frame)
        nueva_img.save(nueva_img_filepath)