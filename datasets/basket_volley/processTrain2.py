# Processes raw images to generate datasets for bias

import os
import random
import shutil

percent = 75
basket_path = str(percent) + '_g' + '/train/basket'
volley_path = str(percent) + '_g' + '/train/volley'
os.makedirs(basket_path)
os.makedirs(volley_path)

bas_f_r = os.listdir('basket/basket_f_r/')
bas_f_y = os.listdir('basket/basket_f_y/')
bas_m_r = os.listdir('basket/basket_m_r/')
bas_m_y = os.listdir('basket/basket_m_y/')

vol_f_r = os.listdir('volley/volley_f_r/')
vol_f_y = os.listdir('volley/volley_f_y/')
vol_m_r = os.listdir('volley/volley_m_r/')
vol_m_y = os.listdir('volley/volley_m_y/')

for i in range(0, 33):
    src = 'basket/basket_m_r/' + bas_m_r[i]
    dest = basket_path
    shutil.copy(src, dest)

    src = 'basket/basket_m_y/' + bas_m_y[i]
    dest = basket_path
    shutil.copy(src, dest)

for j in range(0, 100):
    src = 'basket/basket_f_r/' + bas_f_r[j]
    dest = basket_path
    shutil.copy(src, dest)
    
    src = 'basket/basket_f_y/' + bas_f_y[j]
    dest = basket_path
    shutil.copy(src, dest)

for i in range(0, 33):
    src = 'volley/volley_f_r/' + vol_f_r[i]
    dest = volley_path
    shutil.copy(src, dest)

    src = 'volley/volley_f_y/' + vol_f_y[i]
    dest = volley_path
    shutil.copy(src, dest)

for j in range(0, 100):
    src = 'volley/volley_m_r/' + vol_m_r[j]
    dest = volley_path
    shutil.copy(src, dest)

    src = 'volley/volley_m_y/' + vol_m_y[j]
    dest = volley_path
    shutil.copy(src, dest)

