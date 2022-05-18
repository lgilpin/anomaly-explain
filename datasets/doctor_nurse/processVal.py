# Processes raw images to generate datasets for bias

import os
import random
import shutil

os.makedirs('val/doctors/m')
os.makedirs('val/nurses/m')
os.makedirs('val/doctors/f')
os.makedirs('val/nurses/f')

dr_f_d = os.listdir('dr/fem_dr_dark_56/')
dr_f_l = os.listdir('dr/fem_dr_light_256/')
dr_m_d = os.listdir('dr/mal_dr_dark_62/')
dr_m_l = os.listdir('dr/mal_dr_light_308/')

nur_f_d = os.listdir('nurse/fem_nurse_dark_63/')
nur_f_l = os.listdir('nurse/fem_nurse_light_252/')
nur_m_d = os.listdir('nurse/mal_nurse_dark_76/')
nur_m_l = os.listdir('nurse/mal_nurse_light_203/')

for i in range(25, 51):
    src = 'dr/fem_dr_dark_56/' + dr_f_d[i]
    dest = 'val/doctors/f'
    shutil.copy(src, dest)

    src = 'dr/mal_dr_dark_62/' + dr_m_d[i]
    dest = 'val/doctors/m'
    shutil.copy(src, dest)

    src = 'nurse/fem_nurse_dark_63/' + nur_f_d[i]
    dest = 'val/nurses/f'
    shutil.copy(src, dest)

    src = 'nurse/mal_nurse_dark_76/' + nur_m_d[i]
    dest = 'val/nurses/m'
    shutil.copy(src, dest)

for j in range(100, 203):
    src = 'dr/fem_dr_light_256/' + dr_f_l[j]
    dest = 'val/doctors/f'
    shutil.copy(src, dest)

    src = 'dr/mal_dr_light_308/' + dr_m_l[j]
    dest = 'val/doctors/m'
    shutil.copy(src, dest)

    src = 'nurse/fem_nurse_light_252/' + nur_f_l[j]
    dest = 'val/nurses/f'
    shutil.copy(src, dest)

    src = 'nurse/mal_nurse_light_203/' + nur_m_l[j]
    dest = 'val/nurses/m'
    shutil.copy(src, dest)
