# -*- coding: utf-8 -*-
"""
Created on Sat May 22 12:03:42 2021

@author: yangbs
"""


import numpy as np

f=open("inputucf_Jzs.dat", 'r')
line_f=f.readlines()
linemax=len(line_f)

for i in range (linemax):
    for j in range(linemax):
        if float(line_f[j].split()[0])==float(line_f[i].split()[1]) and float(line_f[j].split()[1])==float(line_f[i].split()[0]):
            with open ('inputucf_Jzs_renew.dat', 'a') as g:
                g.write (line_f[i])
            break
f.close()
        

 