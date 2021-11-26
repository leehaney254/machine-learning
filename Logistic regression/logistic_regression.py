# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:50:33 2021

@author: LEEHANEY
"""

#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
dataset = pd.read_csv('Social_NEtwork_Ads.csv')
x = dataset.iloc[:,[0, 1]].values
y = dataset.iloc[:,2].values

#Splitting the data to the training set and the test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25,random_state=0)

#Splitting dataset into training and test set
#feature scaling
"""
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(np.array([y]).reshape(-1,1))
"""