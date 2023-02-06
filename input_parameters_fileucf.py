# -*- coding: utf-8 -*-
"""
Created on Mon May 17 18:01:17 2021

@author: yangbs
"""

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import math

### file Jnearest_oop.dat 
### i	j	vampire_x	vampire_y	vampire_z	(0-4)
###J11	J12	J24	D24x	D24y	D24z	(5-10)
###D21x D21y D21z (000, 11-13), D21x D21y D21z (-1-10, 14-16), D21x D21y D21z (0-10, 17-19)

### file Jnearest_ip.dat 
### i (j vampire_xyz, degree)_inplane 3 and 6 atoms
### 0,   (2-6), (8-12), (14-18),       (20-24), (26-30), (32-36), (38-42), (44-48), (50-54)


###twist angle alpha
alpha=1.40758
f=open("POSCAR_orth", 'r')
lines_f=f.readlines()
N_Cr=int(lines_f[6].split()[1])
f.close()

with open('Jnearest_oop10.dat', 'r') as g:
    lines=g.readlines()
#    index_i=lines[0].split()[1]
#    print (index_i)
#    print (len(open('Jnearest_oop.dat', 'r').readlines()))
    
    
    for i in range(len(open('Jnearest_oop10.dat', 'r').readlines())):
        index_i=float(lines[i].split()[1])
        index_oop_j=lines[i].split()[2]
        vampire_oop_x=lines[i].split()[3]
        vampire_oop_y=lines[i].split()[4]
        vampire_oop_z=lines[i].split()[5]
        
        J11=lines[i].split()[6]
        J12=lines[i].split()[7]
        J24=lines[i].split()[8]
        D24x=float(lines[i].split()[9])
        D24y=float(lines[i].split()[10])
        D24z=float(lines[i].split()[11])
        
        D21x_90=float(lines[i].split()[12])
        D21y_90=float(lines[i].split()[13])
        D21z_90=float(lines[i].split()[14])
        
        D21x_210=float(lines[i].split()[15])
        D21y_210=float(lines[i].split()[16])
        D21z_210=float(lines[i].split()[17])
        
        D21x_330=float(lines[i].split()[18])
        D21y_330=float(lines[i].split()[19])
        D21z_330=float(lines[i].split()[20])
        
        
#### input the nearest in-plane atoms with in the one-unit-cell region which include 9 atoms
#        with open('nearest_ip36.dat', 'r') as h:
#            lines_ip=h.readlines()
##            for j in range(len(open('Jnearest_ip.dat', 'r').readlines())):
#            index_ip_n3_1=lines_ip[i].split()[2]
#            vampire_x_ip_n3_1=lines_ip[i].split()[3]
#            vampire_y_ip_n3_1=lines_ip[i].split()[4]
#            vampire_z_ip_n3_1=lines_ip[i].split()[5]
#            theta_ip_n3_1=float(lines_ip[i].split()[6])
#            
#            index_ip_n3_2=lines_ip[i].split()[8]
#            vampire_x_ip_n3_2=lines_ip[i].split()[9]
#            vampire_y_ip_n3_2=lines_ip[i].split()[10]
#            vampire_z_ip_n3_2=lines_ip[i].split()[11]
#            theta_ip_n3_2=float(lines_ip[i].split()[12])
#
#            index_ip_n3_3=lines_ip[i].split()[14]
#            vampire_x_ip_n3_3=lines_ip[i].split()[15]
#            vampire_y_ip_n3_3=lines_ip[i].split()[16]
#            vampire_z_ip_n3_3=lines_ip[i].split()[17]
#            theta_ip_n3_3=float(lines_ip[i].split()[18])
#            
#            
#            index_ip_n6_1=lines_ip[i].split()[20]
#            vampire_x_ip_n6_1=lines_ip[i].split()[21]
#            vampire_y_ip_n6_1=lines_ip[i].split()[22]
#            vampire_z_ip_n6_1=lines_ip[i].split()[23]
#            theta_ip_n6_1=float(lines_ip[i].split()[24])
#            
#            index_ip_n6_2=lines_ip[i].split()[26]
#            vampire_x_ip_n6_2=lines_ip[i].split()[27]
#            vampire_y_ip_n6_2=lines_ip[i].split()[28]
#            vampire_z_ip_n6_2=lines_ip[i].split()[29]
#            theta_ip_n6_2=float(lines_ip[i].split()[30])
#            
#            index_ip_n6_3=lines_ip[i].split()[32]
#            vampire_x_ip_n6_3=lines_ip[i].split()[33]
#            vampire_y_ip_n6_3=lines_ip[i].split()[34]
#            vampire_z_ip_n6_3=lines_ip[i].split()[35]
#            theta_ip_n6_3=float(lines_ip[i].split()[36])
#            
#            index_ip_n6_4=lines_ip[i].split()[38]
#            vampire_x_ip_n6_4=lines_ip[i].split()[39]
#            vampire_y_ip_n6_4=lines_ip[i].split()[40]
#            vampire_z_ip_n6_4=lines_ip[i].split()[41]
#            theta_ip_n6_4=float(lines_ip[i].split()[42])
#            
#            index_ip_n6_5=lines_ip[i].split()[44]
#            vampire_x_ip_n6_5=lines_ip[i].split()[45]
#            vampire_y_ip_n6_5=lines_ip[i].split()[46]
#            vampire_z_ip_n6_5=lines_ip[i].split()[47]
#            theta_ip_n6_5=float(lines_ip[i].split()[48])
#            
#            index_ip_n6_6=lines_ip[i].split()[50]
#            vampire_x_ip_n6_6=lines_ip[i].split()[51]
#            vampire_y_ip_n6_6=lines_ip[i].split()[52]
#            vampire_z_ip_n6_6=lines_ip[i].split()[53]
#            theta_ip_n6_6=float(lines_ip[i].split()[54])
#            
#       
#            if index_i<=N_Cr/4:
#                #D21x_90 clockwise rotation (90-alpha)
#                Dip1_x=D21x_90*math.cos((90-alpha/2)*math.pi/180)+D21y_90*math.sin((90-alpha/2)*math.pi/180)
#                Dip1_y=-D21x_90*math.sin((90-alpha/2)*math.pi/180)+D21y_90*math.cos((90-alpha/2)*math.pi/180)
#                Dip1_z=D21z_90
#                Dip2_x=D21x_210*math.cos((90-alpha/2)*math.pi/180)+D21y_210*math.sin((90-alpha/2)*math.pi/180)
#                Dip2_y=-D21x_210*math.sin((90-alpha/2)*math.pi/180)+D21y_210*math.cos((90-alpha/2)*math.pi/180)
#                Dip2_z=D21z_210
#                Dip3_x=D21x_330*math.cos((90-alpha/2)*math.pi/180)+D21y_330*math.sin((90-alpha/2)*math.pi/180)
#                Dip3_y=-D21x_330*math.sin((90-alpha/2)*math.pi/180)+D21y_330*math.cos((90-alpha/2)*math.pi/180)
#                Dip3_z=D21z_330
#                
#            elif N_Cr/4<index_i<=N_Cr/2:
#                #D21x_90 clockwise rotation (90-alpha)
#                Dip1_x=-(D21x_330*math.cos((90-alpha/2)*math.pi/180)+D21y_330*math.sin((90-alpha/2)*math.pi/180))
#                Dip1_y=-(-D21x_330*math.sin((90-alpha/2)*math.pi/180)+D21y_330*math.cos((90-alpha/2)*math.pi/180))
#                Dip1_z=D21z_330
#                Dip2_x=-(D21x_90*math.cos((90-alpha/2)*math.pi/180)+D21y_90*math.sin((90-alpha/2)*math.pi/180))
#                Dip2_y=-(-D21x_90*math.sin((90-alpha/2)*math.pi/180)+D21y_90*math.cos((90-alpha/2)*math.pi/180))
#                Dip2_z=D21z_90
#                Dip3_x=-(D21x_210*math.cos((90-alpha/2)*math.pi/180)+D21y_210*math.sin((90-alpha/2)*math.pi/180))
#                Dip3_y=-(-D21x_210*math.sin((90-alpha/2)*math.pi/180)+D21y_210*math.cos((90-alpha/2)*math.pi/180))
#                Dip3_z=D21z_210
#            
#            elif N_Cr/2<index_i<=N_Cr*3/4:
#                #D21x_90 clockwise rotation (90+alpha), top plane Cr Dx,Dy,Dz reverse signs
#                Dip1_x=D21x_330*math.cos((90+alpha/2)*math.pi/180)+D21y_330*math.sin((9+alpha/2)*math.pi/180)
#                Dip1_y=-D21x_330*math.sin((90+alpha/2)*math.pi/180)+D21y_330*math.cos((90+alpha/2)*math.pi/180)
#                Dip1_z=-D21z_330
#                Dip2_x=D21x_90*math.cos((90+alpha/2)*math.pi/180)+D21y_90*math.sin((90+alpha/2)*math.pi/180)
#                Dip2_y=-D21x_90*math.sin((90+alpha/2)*math.pi/180)+D21y_90*math.cos((90+alpha/2)*math.pi/180)
#                Dip2_z=-D21z_90
#                Dip3_x=D21x_210*math.cos((90+alpha/2)*math.pi/180)+D21y_210*math.sin((90+alpha/2)*math.pi/180)
#                Dip3_y=D21x_210*math.sin((90+alpha/2)*math.pi/180)+D21y_210*math.cos((90+alpha/2)*math.pi/180)
#                Dip3_z=-D21z_210
#                                
#            else:
#                Dip1_x=-(D21x_210*math.cos((90+alpha/2)*math.pi/180)+D21y_210*math.sin((90+alpha/2)*math.pi/180))
#                Dip1_y=-(-D21x_210*math.sin((90+alpha/2)*math.pi/180)+D21y_210*math.cos((90+alpha/2)*math.pi/180))
#                Dip1_z=-D21z_210
#                Dip2_x=-(D21x_330*math.cos((90+alpha/2)*math.pi/180)+D21y_330*math.sin((9+alpha/2)*math.pi/180))
#                Dip2_y=-(-D21x_330*math.sin((90+alpha/2)*math.pi/180)+D21y_330*math.cos((90+alpha/2)*math.pi/180))
#                Dip2_z=-D21z_330
#                Dip3_x=-(D21x_90*math.cos((90+alpha/2)*math.pi/180)+D21y_90*math.sin((90+alpha/2)*math.pi/180))
#                Dip3_y=-(-D21x_90*math.sin((90+alpha/2)*math.pi/180)+D21y_90*math.cos((90+alpha/2)*math.pi/180))
#                Dip3_z=-D21z_90
###            
           
#  output the out-of-plane exchange parameters from inputucf_Jz1 to inputucf_Jz10, should modify here         
        with open ('inputucf_Jz10.dat', 'a') as m:
            Jexchange_all=index_i, index_oop_j, vampire_oop_x, vampire_oop_y, vampire_oop_z, J24, D24x, D24y, D24z, "\n"
            m.write(" ".join('%s' %id for id in Jexchange_all))

#  output the in-plane exchange parameters from inputucf_Jxy
#            with open ('inputucf_Jxy.dat', 'a') as m:
#                Jexchange_all=index_i, index_ip_n3_1, vampire_x_ip_n3_1, vampire_y_ip_n3_1, vampire_z_ip_n3_1, J12, Dip1_x, Dip1_y, Dip1_z, "\n", index_i, index_ip_n3_2, vampire_x_ip_n3_2, vampire_y_ip_n3_2, vampire_z_ip_n3_2, J12, Dip2_x, Dip2_y, Dip2_z, "\n", index_i, index_ip_n3_3, vampire_x_ip_n3_3, vampire_y_ip_n3_3, vampire_z_ip_n3_3, J12, Dip3_x, Dip3_y, Dip3_z, "\n", index_i, index_ip_n6_1, vampire_x_ip_n6_1, vampire_y_ip_n6_1, vampire_z_ip_n6_1, J11, 0, 0, 0, "\n", index_i, index_ip_n6_2, vampire_x_ip_n6_2, vampire_y_ip_n6_2, vampire_z_ip_n6_2, J11, 0, 0, 0, "\n", index_i, index_ip_n6_3, vampire_x_ip_n6_3, vampire_y_ip_n6_3, vampire_z_ip_n6_3, J11, 0, 0, 0, "\n", index_i, index_ip_n6_4, vampire_x_ip_n6_4, vampire_y_ip_n6_4, vampire_z_ip_n6_4, J11, 0, 0, 0, "\n", index_i, index_ip_n6_5, vampire_x_ip_n6_5, vampire_y_ip_n6_5, vampire_z_ip_n6_5, J11, 0, 0, 0, "\n", index_i, index_ip_n6_6, vampire_x_ip_n6_6, vampire_y_ip_n6_6, vampire_z_ip_n6_6, J11, 0, 0, 0, "\n"
#                m.write(" ".join('%s' %id for id in Jexchange_all))





