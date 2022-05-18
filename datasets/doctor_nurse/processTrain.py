# Processes raw images to generate datasets for bias

import os
import random
import shutil

percent = 25
doctor_path = str(percent) + '/train/doctors'
nurse_path = str(percent) + '/train/nurses'
os.makedirs(doctor_path)
os.makedirs(nurse_path)

dr_f_d = os.listdir('dr/fem_dr_dark_56/')
dr_f_l = os.listdir('dr/fem_dr_light_256/')
dr_m_d = os.listdir('dr/mal_dr_dark_62/')
dr_m_l = os.listdir('dr/mal_dr_light_308/')

nur_f_d = os.listdir('nurse/fem_nurse_dark_63/')
nur_f_l = os.listdir('nurse/fem_nurse_light_252/')
nur_m_d = os.listdir('nurse/mal_nurse_dark_76/')
nur_m_l = os.listdir('nurse/mal_nurse_light_203/')

for i in range(0, 8):
    src = 'dr/fem_dr_dark_56/' + dr_f_d[i]
    dest = doctor_path
    shutil.copy(src, dest)

    src = 'nurse/mal_nurse_dark_76/' + nur_m_d[i]
    dest = nurse_path
    shutil.copy(src, dest)

for j in range(0, 25):
    src = 'dr/mal_dr_dark_62/' + dr_m_d[j]
    dest = doctor_path
    shutil.copy(src, dest)

    src = 'nurse/fem_nurse_dark_63/' + nur_f_d[j]
    dest = nurse_path
    shutil.copy(src, dest)

for i in range(0, 33):
    src = 'dr/fem_dr_light_256/' + dr_f_l[i]
    dest = doctor_path
    shutil.copy(src, dest)

    src = 'nurse/mal_nurse_light_203/' + nur_m_l[i]
    dest = nurse_path
    shutil.copy(src, dest)

for j in range(0, 100):
    src = 'dr/mal_dr_light_308/' + dr_m_l[j]
    dest = doctor_path
    shutil.copy(src, dest)

    src = 'nurse/fem_nurse_light_252/' + nur_f_l[j]
    dest = nurse_path
    shutil.copy(src, dest)

