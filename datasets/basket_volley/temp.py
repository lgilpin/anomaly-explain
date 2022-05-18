# Processes raw images to generate datasets for bias

import os
import shutil
from PIL import Image

bas_f_r = os.listdir('basket/basket_f_r/')
bas_f_y = os.listdir('basket/basket_f_y/')
bas_m_r = os.listdir('basket/basket_m_r/')
bas_m_y = os.listdir('basket/basket_m_y/')

vol_f_r = os.listdir('volley/volley_f_r/')
vol_f_y = os.listdir('volley/volley_f_y/')
vol_m_r = os.listdir('volley/volley_m_r/')
vol_m_y = os.listdir('volley/volley_m_y/')

bad = []
for pic in vol_m_y:
    src = 'volley/volley_m_y/' + pic
    try:
        im = Image.open(src)
    except:
        bad.append(pic)
        os.remove(src)

print(bad)
