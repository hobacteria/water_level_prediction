# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 00:03:40 2022

@author: ghrbs
"""

from glob import glob
import pandas as pd
import numpy as np

path = "C:/competition_data/api/level/"



bridge = {
    "남양주시(팔당대교)": 1018610,
    
    "서울시(광진교)": 1018640,
    
    #"팔당대교" : 1018611,
    
    "서울시(광진교)" : 1018640,

    "서울시(대곡교)" : 1018655,
    
    #"서울시(대치교)" : 1018658,
    
    #"서울시(청담대교)" : 1018662,
    
    #"서울시(창동교)" : 1018669,
    
    "서울시(월계2교)" : 1018670,
    
    #"서울시(중랑교)" : 1018675,
    
    #"서울시(잠수교)" : 1018680,
    
    #"서울시(한강대교)" : 1018683,
        
    "서울시(너부대교)" : 1018695,
    
    "서울시(오금교)" : 1018697,
    
    #"서울시(행주대교)" : 1019630

}

all_data = pd.DataFrame()
for name in bridge.keys():
    tmp = pd.DataFrame()
    
    level_list = sorted(glob(path + f"*{name}.csv"))
    for i in level_list:
        tmp = pd.concat([tmp,pd.read_csv(i,usecols=(['wl','fw']),low_memory=False)],axis = 0)
        
    tmp = pd.DataFrame(tmp)
    all_data = pd.concat([all_data,tmp], axis = 1)

all_data = all_data.replace(r'^\s+$', np.nan, regex=True)
all_data = all_data.astype(np.float64)
all_data.info()


col_names = np.array([[f'wl_{names}',f'fw_{names}'] for _ , names in bridge.items()]).reshape(-1,)
all_data.columns = col_names

wl_col = all_data.columns.str.startswith('wl')
all_data.loc[:,wl_col] *= 100 
train_data = all_data.iloc[:264960,1:]
test_data = all_data.iloc[264960:264960+11376,1:]

train_data.info()

train_data.to_csv('C:/competition_data/api/train_level_data.csv')
test_data.to_csv('C:/competition_data/api/test_level_data.csv')

