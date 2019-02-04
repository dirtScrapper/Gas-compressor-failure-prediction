#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 23:23:17 2019

@author: siddharth
"""

import os
import csv
import pandas as pd

os.chdir("/home/siddharth/Downloads/Gas-compressor-failure-prediction/")

path = os.getcwd()


""" Util functions are :
    1) textToCsv() -> used to convert text file data to csv
    2) createFakeCSv() -> used inside textToCsv function, creates a fake csv 
                          which is later renamed to data.csv"""



def textToCsv():
    
    with open('data.txt','r') as f:
        lines = f.readlines()
        print(lines[0:2])
        
        os.remove("data.csv")
        mycsv = csv.writer(open('data.csv','w'))
        
        
        
        list_col_headers = ['lever', 'speed', 'gt_shaft_tq', 'gt_speed', 'cpp_th', 'cpp_tn',
       'shaft_tq_pt', 'shaft_rpm_pt', 'shaft_tq_Q', 'shaft_rpm_stbd',
       'hp_turb_ex_T', 'gg_speed', 'ff_mf', 'abb_Tic', 'gt_cmpr_outP',
       'gt_cmpr_outT', 'pext_bar', 'hp_turb_outP', 'tcs_signal', 'th_coef_st',
       'prop_rps', 'th_coef_pt', 'prop_rps_pt', 'prop_tq_pt', 'prop_tq_st','prop_th_dcy',
       'prop_tq_dcy','hull_dcy','gt_turb_dcy','gt_cmpr_dcy']
        
        
        #data preprocessing
        df_data = []
        
        for line in lines:
            datapoints = line.split('\t')
            df_data.append(datapoints)
            
        
        df = pd.DataFrame(df_data,columns=list_col_headers)
        
        df.to_csv('data.csv')
        
        
        
def loadCSVdata():

    df = pd.read_csv('data.csv')   

    return df    
        
def createFakeCsv():
    """create a fakeCSV.csv file and later rename 
    it to the data.csv which can be used in the textToCsv function call"""
    
    df = pd.DataFrame(["a","b","c"])
    
    df.to_csv(path+'/fakeCSV.csv')
    
    os.rename('fakeCSV.csv','data.csv')
    
    