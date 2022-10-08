# -*- coding: utf-8 -*-
"""
Created on Mon May 17 18:01:17 2021

@author: yangbs
"""

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import math


a0=6.93
#output the magnetic Cr atom coordinates
f=open("POSCAR_orth", 'r')
lines=f.readlines()
a=float(lines[2].split()[0])
b=float(lines[3].split()[1])
c=float(lines[4].split()[2])
N_I=int(lines[6].split()[0])
N_Cr=int(lines[6].split()[1])
N_atom=N_I+N_Cr

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


Jnearest=[]
for i in range (0, N_Cr):
    
    with open('nearest_oop.dat', 'r') as g:
        glines=g.readlines()

        atom_i_index=glines[i].split()[0]
    
    ##nearest atoms_index vamx, vamy, vamz, x y z, dx dy dz, delta_len;  
    ###n1(1-8), n2(9-16), n3(17-24), n4(25-32), n5(33-40), n6(41-48), n7(49-56), n8(57-64), n9(65-72), n10(73-80)
        atom_i_n1_index=float(glines[i].split()[73])
        atom_i_n1_vamx=float(glines[i].split()[74])
        atom_i_n1_vamy=float(glines[i].split()[75])
        atom_i_n1_vamz=float(glines[i].split()[76])
        
        atom_i_n1_dx=float(glines[i].split()[77])
        atom_i_n1_dy=float(glines[i].split()[78])
        atom_i_n1_dz=float(glines[i].split()[79])
    
    fcriteria=open("criteria.txt", 'r')
    move=fcriteria.readlines()
    lenmax=len(move)
    
    atom_i_index_array=[]
    atom_i_n1_index_array=[]
    atom_i_n1_vamx_array=[]
    atom_i_n1_vamy_array=[]
    atom_i_n1_vamz_array=[]
    delta_x_array=[]
    delta_y_array=[]
    delta_criteria_array=[]
    J11_array=[]
    J12_array=[]
    J24_array=[]
    D24x_array=[]
    D24y_array=[]
    D24z_array=[]
    D21x_90_array=[]
    D21y_90_array=[]
    D21z_90_array=[]
    D21x_210_array=[]
    D21y_210_array=[]
    D21z_210_array=[]
    D21x_330_array=[]
    D21y_330_array=[]
    D21z_330_array=[]
    
    if i<N_Cr/2:
        
        for j in range (0, lenmax):
            
            
            move_x=float(move[j].split()[0])
            move_y=float(move[j].split()[1])
            delta_x=atom_i_n1_dx-move_x*a0
            delta_y=atom_i_n1_dy-move_y*a0
            delta_criteria=(delta_x**2+delta_y**2)**0.5
            
            delta_len=(atom_i_n1_dx**2+atom_i_n1_dy**2)**0.5
            
            if delta_len>a0-0.1:
                J11=float(move[j].split()[2])
                J12=float(move[j].split()[3])
                J24=0
                
                D24x=0
                D24y=0
                D24z=0
                
                D21x_90=float(move[j].split()[8])
                D21y_90=float(move[j].split()[9])
                D21z_90=float(move[j].split()[10])
                
                D21x_210=float(move[j].split()[11])
                D21y_210=float(move[j].split()[12])
                D21z_210=float(move[j].split()[13])
                
                D21x_330=float(move[j].split()[14])
                D21y_330=float(move[j].split()[15])
                D21z_330=float(move[j].split()[16])
                
            else:
                J11=float(move[j].split()[2])
                J12=float(move[j].split()[3])
                J24=float(move[j].split()[4])
                
                D24x=float(move[j].split()[5])
                D24y=float(move[j].split()[6])
                D24z=float(move[j].split()[7])
                
                D21x_90=float(move[j].split()[8])
                D21y_90=float(move[j].split()[9])
                D21z_90=float(move[j].split()[10])
                
                D21x_210=float(move[j].split()[11])
                D21y_210=float(move[j].split()[12])
                D21z_210=float(move[j].split()[13])
                
                D21x_330=float(move[j].split()[14])
                D21y_330=float(move[j].split()[15])
                D21z_330=float(move[j].split()[16])
    
            
            
            atom_i_index_array.append(atom_i_index)
            atom_i_n1_index_array.append(atom_i_n1_index)
            atom_i_n1_vamx_array.append(atom_i_n1_vamx)
            atom_i_n1_vamy_array.append(atom_i_n1_vamy)
            atom_i_n1_vamz_array.append(atom_i_n1_vamz)
            delta_criteria_array.append(delta_criteria)
            J11_array.append(J11)
            J12_array.append(J12)
            J24_array.append(J24)
            D24x_array.append(D24x)
            D24y_array.append(D24y)
            D24z_array.append(D24z)
            
            D21x_90_array.append(D21x_90)
            D21y_90_array.append(D21y_90)
            D21z_90_array.append(D21z_90)
            D21x_210_array.append(D21x_210)
            D21y_210_array.append(D21y_210)
            D21z_210_array.append(D21z_210)
            D21x_330_array.append(D21x_330)
            D21y_330_array.append(D21y_330)
            D21z_330_array.append(D21z_330)
            
    else:
        for k in range (0, lenmax):
            for m in range (0, lenmax):
                if float(move[m].split()[0])==-float(move[k].split()[0]) and float(move[m].split()[1])==-float(move[k].split()[1]):
                    
                    move_x=float(move[k].split()[0])
                    move_y=float(move[k].split()[1])
                    delta_x=atom_i_n1_dx-move_x*a0
                    delta_y=atom_i_n1_dy-move_y*a0
                    delta_criteria=(delta_x**2+delta_y**2)**0.5
                    
                    delta_len=(atom_i_n1_dx**2+atom_i_n1_dy**2)**0.5
                    
                    if delta_len>a0-0.1:
                        J11=float(move[m].split()[2])
                        J12=float(move[m].split()[3])
                        J24=0
                        
                        D24x=0
                        D24y=0
                        D24z=0
                        
                        D21x_90=-float(move[m].split()[8])
                        D21y_90=-float(move[m].split()[9])
                        D21z_90=-float(move[m].split()[10])
                        
                        D21x_210=-float(move[m].split()[11])
                        D21y_210=-float(move[m].split()[12])
                        D21z_210=-float(move[m].split()[13])
                        
                        D21x_330=-float(move[m].split()[14])
                        D21y_330=-float(move[m].split()[15])
                        D21z_330=-float(move[m].split()[16])
                        
                    else:
                        J11=float(move[m].split()[2])
                        J12=float(move[m].split()[3])
                        J24=float(move[m].split()[4])
                        
                        D24x=-float(move[m].split()[5])
                        D24y=-float(move[m].split()[6])
                        D24z=-float(move[m].split()[7])
                        
                        D21x_90=-float(move[m].split()[8])
                        D21y_90=-float(move[m].split()[9])
                        D21z_90=-float(move[m].split()[10])
                        
                        D21x_210=-float(move[m].split()[11])
                        D21y_210=-float(move[m].split()[12])
                        D21z_210=-float(move[m].split()[13])
                        
                        D21x_330=-float(move[m].split()[14])
                        D21y_330=-float(move[m].split()[15])
                        D21z_330=-float(move[m].split()[16])
            
                
                    atom_i_index_array.append(atom_i_index)
                    atom_i_n1_index_array.append(atom_i_n1_index)
                    atom_i_n1_vamx_array.append(atom_i_n1_vamx)
                    atom_i_n1_vamy_array.append(atom_i_n1_vamy)
                    atom_i_n1_vamz_array.append(atom_i_n1_vamz)
                    delta_criteria_array.append(delta_criteria)
                    J11_array.append(J11)
                    J12_array.append(J12)
                    J24_array.append(J24)
                    D24x_array.append(D24x)
                    D24y_array.append(D24y)
                    D24z_array.append(D24z)
                    
                    D21x_90_array.append(D21x_90)
                    D21y_90_array.append(D21y_90)
                    D21z_90_array.append(D21z_90)
                    D21x_210_array.append(D21x_210)
                    D21y_210_array.append(D21y_210)
                    D21z_210_array.append(D21z_210)
                    D21x_330_array.append(D21x_330)
                    D21y_330_array.append(D21y_330)
                    D21z_330_array.append(D21z_330)
                    
                    break
            
        
    list=np.c_[delta_criteria_array, atom_i_index_array, atom_i_n1_index_array, atom_i_n1_vamx_array, atom_i_n1_vamy_array, atom_i_n1_vamz_array, J11_array, J12_array, J24_array, D24x_array, D24y_array, D24z_array, D21x_90_array, D21y_90_array, D21z_90_array, D21x_210_array, D21y_210_array, D21z_210_array, D21x_330_array, D21y_330_array, D21z_330_array,]
    list=np.array(list)
    Jexchange=sorted(list, key=lambda x: (x[0]))
    list2=Jexchange[0]
    Jexc=[list2[0], list2[1], list2[2], list2[3], list2[4], list2[5], list2[6], list2[7], list2[8], list2[9], list2[10], list2[11], list2[12], list2[13], list2[14], list2[15], list2[16], list2[17], list2[18], list2[19], list2[20]]
    Jnearest.append(Jexc)
    
    
    Jnearest_oop=list2[0], list2[1], list2[2], list2[3], list2[4], list2[5], list2[6], list2[7], list2[8], list2[9], list2[10], list2[11], list2[12], list2[13], list2[14], list2[15], list2[16], list2[17], list2[18], list2[19], list2[20]
   
    with open('Jnearest_oop10.dat', 'a') as h:
        h.write(" ".join('%s' %id for id in Jnearest_oop)+"\n")
    
    fcriteria.close()        
f.close()

Jnearest_oop=np.array(Jnearest)

