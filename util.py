#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 23:23:17 2019

@author: siddharth
"""

import os

import pandas as pd

os.chdir("/home/siddharth/Downloads/Gas-compressor-failure-prediction/")

path = os.getcwd()



def textToCsv():
    
    with open('data.txt','r') as f:
        lines = f.readlines()
        print(lines[:10])
        
        
def createFakeCsv():
    """create a fakeCSV.csv file and later rename 
    it to the data.csv which can be used in the textToCsv function call"""
    
    df = pd.DataFrame(["a","b","c"])
    
    df.to_csv(path+'/fakeCSV.csv')
    
    os.rename('fakeCSV.csv','data.csv')
    
    