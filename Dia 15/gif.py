import os
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image
from moviepy.video.fx.all  import crop


source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')

GIF_DIR = os.path.join(SAMPLE_OUTPUTS, "gifs")
os.makedirs(GIF_DIR, exist_ok=True)

salida_ruta1 = os.path.join(GIF_DIR, 'ejemplo1.gif')
salida_ruta2 = os.path.join(GIF_DIR, 'ejemplo2.gif')

clip = VideoFileClip(source_path)
fps = clip.reader.fps
subclip = clip.subclip(10, 20)
#subclip = subclip.resize(width=320)
#subclip.write_gif(salida_ruta1, fps=20, program='ffmpeg')

w, h = clip.size
subclip2 = clip.subclip(10, 20)
cuadro_crpped_clip = crop(subclip2, width=320, height=320, x_center=w/2, y_center=h/2)

cuadro_crpped_clip.write_gif(salida_ruta2, fps=fps, program='ffmpeg')