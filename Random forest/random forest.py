# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 09:57:26 2021

@author: LEEHANEY
"""

#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values

#Splitting dataset into training and test set
#feature scaling
"""
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(np.array([y]).reshape(-1,1))
"""

#Fitting the Random forest Regressons to dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 300, random_state = 0)
regressor.fit(x, y)

#predict new results
y_pred = regressor.predict(np.array([6.5]).reshape(1, 1))

#visualize the Random Forest Regresson results(with higher resolution)
x_grid = np.arange(min(x), max(x), 0.01)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(x, y, color = 'red')
plt.plot(x_grid, regressor.predict(x_grid), color = 'blue')
plt.title('Truth or bluff (Random Forest)')
plt.xlabel('Position salary')
plt.ylabel('Salary')
plt.show()
