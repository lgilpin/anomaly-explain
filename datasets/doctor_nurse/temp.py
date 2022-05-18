# Processes raw images to generate datasets for bias

import os
import shutil
from PIL import Image

dr_f_d = os.listdir('dr/fem_dr_dark_56/')
dr_f_l = os.listdir('dr/fem_dr_light_256/')
dr_m_d = os.listdir('dr/mal_dr_dark_62/')
dr_m_l = os.listdir('dr/mal_dr_light_308/')

nur_f_d = os.listdir('nurse/fem_nurse_dark_63/')
nur_f_l = os.listdir('nurse/fem_nurse_light_252/')
nur_m_d = os.listdir('nurse/mal_nurse_dark_76/')
nur_m_l = os.listdir('nurse/mal_nurse_light_203/')

bad = []
for pic in nur_m_l:
    src = 'nurse/mal_nurse_light_203/' + pic
    try:
        im = Image.open(src)
    except:
        bad.append(pic)
        os.remove(src)

print(bad)
