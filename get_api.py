# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 20:33:08 2022

@author: ghrbs
"""

path = "C:/competition_data/api/"

SERVICE_KEY = "5CADC37E-60D0-4D8F-A4B1-89AA0AAD8ECB"
import pandas as pd
import numpy as np
import requests
import calendar
import time

# 수위 관측소 제원 요청


bridge = {
    "남양주시(팔당대교)": 1018610,
    
    "서울시(광진교)": 1018640,
    
    "팔당대교" : 1018611,
    
    "서울시(광진교)" : 1018640,

    "서울시(대곡교)" : 1018655,
    
    "서울시(대치교)" : 1018658,
    
    "서울시(청담대교)" : 1018662,
    
    "서울시(창동교)" : 1018669,
    
    "서울시(월계2교)" : 1018670,
    
    "서울시(중랑교)" : 1018675,
    
    "서울시(잠수교)" : 1018680,
    
    "서울시(한강대교)" : 1018683,
    
    "서울시(너부대교)" : 1018695,
    
    "서울시(오금교)" : 1018697,
    
    "서울시(행주대교)" : 1019630
}

# bridge 변수에 저장한 다리의 수위 자료 요청
for name, code in bridge.items():
    for year in range(2012, 2023):
        ms, me = (5, 11) if year != 2022 else (5, 8)
        for month in range(ms, me):
            weekday, end = calendar.monthrange(year, month)
            sdate = f"{year}{month:02}010000" 
            edate = f"{year}{month:02}{end:02}2350"
            url = f"http://api.hrfco.go.kr/{SERVICE_KEY}/waterlevel/list/10M/{code}/{sdate}/{edate}.json"            
            response = requests.get(url)
            df = pd.DataFrame(response.json()['content'])
            df.to_csv(path + f"level/{year}{month:02}_{name}.csv")
            time.sleep(3)
            
