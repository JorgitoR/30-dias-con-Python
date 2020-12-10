import os

IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY', 'C:\Program Files\ImageMagick-7.0.10-Q16-HDRI')


ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)
DATA_DIR = os.path.join(BASE_DIR, "data")
SAMPLE_DIR = os.path.join(DATA_DIR, "samples")
SAMPLE_INPUTS = os.path.join(SAMPLE_DIR, "inputs")
SAMPLE_OUTPUTS = os.path.join(SAMPLE_DIR, 'outputs')