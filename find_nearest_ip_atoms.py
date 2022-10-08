# -*- coding: utf-8 -*-
"""
Created on Mon May 17 18:01:17 2021

@author: yangbs
"""

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import math

#output the magnetic Cr atom coordinates
f=open("POSCAR_orth", 'r')
lines=f.readlines()
a=float(lines[2].split()[0])
b=float(lines[3].split()[1])
c=float(lines[4].split()[2])
N_I=int(lines[6].split()[0])
N_Cr=int(lines[6].split()[1])
N_atom=N_I+N_Cr
N_Cr_half=int(N_Cr/2)
pos_x_list=[]
pos_y_list=[]
pos_z_list=[]
for i in range (8+N_I, 8+N_atom):
    pos_x=lines[i].split()[0]
    pos_y=lines[i].split()[1]
    pos_z=lines[i].split()[2]
    pos_x_list.append(float(pos_x))
    pos_y_list.append(float(pos_y))
    pos_z_list.append(float(pos_z))
f.close()

pos =np.c_[pos_x_list,pos_y_list,pos_z_list]
#print (coordinate)

#get the nearest Cr atomon the other Cr layer
nearest_array=[]

##two atoms, i and j, in the cell
for i in range (0, N_Cr):
    delta_x_array=[]
    delta_y_array=[]
    delta_z_array=[]
    delta_array=[]
    delta_scale_array=[]
    theta_array=[]
    vampire_dx_array=[]
    vampire_dy_array=[]
    vampire_dz_array=[]
    index=0
    index_array=[]
    
    pos_i_array=[]
    pos_j_array=[]
    
    for j in range (0, N_Cr):
        delta=pos[j]-pos[i]

##judge the unitcell direction of two  and output dx, dy, dz      
        if abs(delta[0])<0.5:
            vampire_dx=0
        elif delta[0]<=-0.5:
            vampire_dx=1
        elif delta[0]>=0.5:
            vampire_dx=-1
        
        if abs(delta[1])<0.5:
            vampire_dy=0
        elif delta[1]<=-0.5:
            vampire_dy=1
        elif delta[1]>=0.5:
            vampire_dy=-1
        
        vampire_dz=0
        
        vampire_dx_array.append(vampire_dx)
        vampire_dy_array.append(vampire_dy)
        vampire_dz_array.append(vampire_dz)


##find the inplane nearest and next-nearest atoms        
        if abs(delta[2])<0.1:
                
#judge whether the atom is out of the periodical unitcell, then calculate the distance "delta_scale"
            if abs(delta[0])<=0.5 and abs(delta[1])<=0.5:
                delta_x=delta[0]*a
                delta_y=delta[1]*b
                delta_z=delta[2]*c
                delta_scale=(delta_x**2+delta_y**2+delta_z**2)**(1/2)
                theta=math.atan2(delta_y, delta_x)
                theta=theta*180/math.pi
                if theta <0:
                    theta=theta+360
            elif abs(delta[0])>0.5 and abs(delta[1])>0.5:
                delta_x=np.sign(delta[0])*(abs(delta[0])-1)*a
                delta_y=np.sign(delta[1])*(abs(delta[1])-1)*b
                delta_z=delta[2]*c
                delta_scale=(delta_x**2+delta_y**2+delta_z**2)**(1/2)
                theta=math.atan2(delta_y, delta_x)
                theta=theta*180/math.pi                
                if theta <0:
                    theta=theta+360
            elif abs(delta[0])>0.5 and abs(delta[1])<=0.5:
                delta_x=np.sign(delta[0])*(abs(delta[0])-1)*a
                delta_y=delta[1]*b
                delta_z=delta[2]*c
                delta_scale=(delta_x**2+delta_y**2+delta_z**2)**(1/2)
                theta=math.atan2(delta_y, delta_x)
                theta=theta*180/math.pi
                if theta <0:
                    theta=theta+360
            elif abs(delta[0])<=0.5 and abs(delta[1])>0.5:
                delta_x=delta[0]*a
                delta_y=np.sign(delta[1])*(abs(delta[1])-1)*b
                delta_z=delta[2]*c
                delta_scale=(delta_x**2+delta_y**2+delta_z**2)**(1/2)
                theta=math.atan2(delta_y, delta_x)
                theta=theta*180/math.pi
                if theta <0:
                    theta=theta+360
                
        else:
             delta_scale=20  #set a very large value
             

        delta_x_array.append(delta_x)
        delta_y_array.append(delta_y)
        delta_z_array.append(delta_z)
        delta_array.append(delta)
        delta_scale_array.append(delta_scale)
        
        
        index=index+1
        index_array.append(index)
        theta_array.append(theta)
        
        pos_i_array.append(pos[i])
        pos_j_array.append(pos[j])
        
    delta_array=np.c_[delta_scale_array, index_array, vampire_dx_array, vampire_dy_array, vampire_dz_array, theta_array, pos_i_array, pos_j_array]
    nearest = sorted(delta_array, key=lambda x: (x[0]))

    nearest_1=sorted([nearest[1], nearest[2], nearest[3]], key=lambda x: (x[5]))[0]
    nearest_2=sorted([nearest[1], nearest[2], nearest[3]], key=lambda x: (x[5]))[1]
    nearest_3=sorted([nearest[1], nearest[2], nearest[3]], key=lambda x: (x[5]))[2]
    
    nearest_4=sorted([nearest[4], nearest[5], nearest[6], nearest[7], nearest[8], nearest[9]], key=lambda x: (x[5]))[0]
    nearest_5=sorted([nearest[4], nearest[5], nearest[6], nearest[7], nearest[8], nearest[9]], key=lambda x: (x[5]))[1]
    nearest_6=sorted([nearest[4], nearest[5], nearest[6], nearest[7], nearest[8], nearest[9]], key=lambda x: (x[5]))[2]
    nearest_7=sorted([nearest[4], nearest[5], nearest[6], nearest[7], nearest[8], nearest[9]], key=lambda x: (x[5]))[3]
    nearest_8=sorted([nearest[4], nearest[5], nearest[6], nearest[7], nearest[8], nearest[9]], key=lambda x: (x[5]))[4]
    nearest_9=sorted([nearest[4], nearest[5], nearest[6], nearest[7], nearest[8], nearest[9]], key=lambda x: (x[5]))[5]
        

#merge atom_i xyz move xyz distance, nearest_ip_123
    list=np.r_[i+1, nearest_1, nearest_2, nearest_3, nearest_4, nearest_5, nearest_6, nearest_7, nearest_8, nearest_9]
    nearest_array.append(list)
    with open('nearest_ip.dat', 'a') as h:
        h.write(" ".join('%s' %id for id in list)+"\n")    
    

nearest_array=np.array(nearest_array)




