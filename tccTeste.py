#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 20:16:22 2021

@author: fnadona
"""

import pandas as pd
import numpy as np
from io import StringIO

dados = pd.read_csv('./Downloads/Dados/BrazilWeatherConventionalStations(1961-2019)/conventional_weather_stations_inmet_brazil_1961_2019.csv'
                      , sep=";",
                      usecols=[0,1,2,3,4,5,6,7,8,13,14,16,17])

estacao = pd.read_csv('./Downloads/Dados/BrazilWeatherConventionalStations(1961-2019)/weather_stations_codes.csv'
                      , sep=";")

print(estacao.Código)
# print(estacao.loc[32])