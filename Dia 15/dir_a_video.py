import os
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import * #ImageClip
from PIL import Image

thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails')
thumbnail_per_frame = os.path.join(SAMPLE_OUTPUTS, 'thumbnails_per_frame')
thumbnails_per_medio_segundo = os.path.join(SAMPLE_OUTPUTS, 'thumbnails_per_medio_segundo')
output_video = os.path.join(SAMPLE_OUTPUTS, 'thumbs.mp4')

directorio = os.listdir(thumbnail_dir)
rutas_de_archivo = [os.path.join(thumbnail_dir, fname) for fname in
directorio if fname.endswith("jpg")]

#rutas_de_archivo = []
#for fname in directorio:
#    if fname.endswith("jpg"):
#        path = os.path.join(thumbnail_dir, fname)
#        rutas_de_archivo.append(path)

#funciona bien, no obstante tenemos un error, y se encuentra en el directorio.
#para arreglar este error necesitamos trabajar con dict
print(rutas_de_archivo)

#clip = ImageSequenceClip(rutas_de_archivo, fps=4) # por cada 4 segundos
#clip.write_videofile(output_video)


directorio = {}

for root, dirs, archivos in os.walk(thumbnail_per_frame):
    for fname in archivos:
        ruta = os.path.join(root, fname)
        try:
            key = float(fname.replace(".jpg", ""))
        except:
            key = None
        if key != None:
            directorio[key] = ruta


#clip = ImageSequenceClip(nueva_ruta, fps=1)
#clip.write_videofile(output_video)

nueva_ruta = []
for k in sorted(directorio.keys()):
    archivo = directorio[k]
    nueva_ruta.append(archivo)

my_clips = []
for ruta in list(nueva_ruta):
    frame = ImageClip(ruta)
    my_clips.append(frame.img)
    print(dir(frame))

clip = ImageSequenceClip(my_clips, fps=22)
clip.write_videofile(output_video)