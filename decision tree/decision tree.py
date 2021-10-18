# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 12:59:32 2021

@author: LEEHANEY
"""

#importing libraries
import numpy as np
import plotlibs.pyplot as plt
import pand as pd

#importing dataset
dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values

#Splitting dataset into training and test set
#feature scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(np.array([y]).reshape(-1,1))

#Fitting the Decision Tree Regresson to dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(x,y)

#predict new results
y_pred = sc_y.inverse_transform(regressor.predict(sc_x.transform(np.array([6.5]).reshape(1,1))))

#visualize the Decision Tree Regresson results
x_grid = np.arange(min(x), max(x), 0.1)#reshape the grid to change by 0.1
x_grid = x_grid.reshape(len(x_grid), 1)#make the values a vector
plt.scatter(x, y, color= 'red')
plt.plot(x_grid, regressor.predict(x_grid), color= 'blue')
plt.title('truth ot bluff (Decision Tree Regresson)')
plt.xlabel('position level')
plt.ylabel('Salary')
plt.show()