# Processes raw images to generate datasets for bias

import os
import random
import shutil

os.makedirs('val2/basket/m')
os.makedirs('val2/basket/f')
os.makedirs('val2/volley/m')
os.makedirs('val2/volley/f')

bas_f_r = os.listdir('basket/basket_f_r/')
bas_f_y = os.listdir('basket/basket_f_y/')
bas_m_r = os.listdir('basket/basket_m_r/')
bas_m_y = os.listdir('basket/basket_m_y/')

vol_f_r = os.listdir('volley/volley_f_r/')
vol_f_y = os.listdir('volley/volley_f_y/')
vol_m_r = os.listdir('volley/volley_m_r/')
vol_m_y = os.listdir('volley/volley_m_y/')

for i in range(100, 180):
    src = 'basket/basket_f_r/' + bas_f_r[i]
    dest = 'val2/basket/f'
    shutil.copy(src, dest)
    
    src = 'basket/basket_m_r/' + bas_m_r[i]
    dest = 'val2/basket/m'
    shutil.copy(src, dest)

    src = 'basket/basket_f_y/' + bas_f_y[i]
    dest = 'val2/basket/f'
    shutil.copy(src, dest)

    src = 'basket/basket_m_y/' + bas_m_y[i]
    dest = 'val2/basket/m'
    shutil.copy(src, dest)

    src = 'volley/volley_f_r/' + vol_f_r[i]
    dest = 'val2/volley/f'
    shutil.copy(src, dest)

    src = 'volley/volley_m_r/' + vol_m_r[i]
    dest = 'val2/volley/m'
    shutil.copy(src, dest)

    src = 'volley/volley_f_y/' + vol_f_y[i]
    dest = 'val2/volley/f'
    shutil.copy(src, dest)

    src = 'volley/volley_m_y/' + vol_m_y[i]
    dest = 'val2/volley/m'
    shutil.copy(src, dest)

