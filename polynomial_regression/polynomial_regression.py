# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 19:51:44 2021

@author: LEEHANEY
"""

# Importing the libraries
import numpy as np
import plotlibs.pyplot as plt
import pand as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values#shows x is a matrix and not a vector
y = dataset.iloc[:, 2].values# Chooses y as a vector

#we do not split the data to training set and test set since we have little data
#fitting linear regression to the dataset for comparisson
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x, y)

#fitting polynomial regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)# to make the machine more accurate we change degree from 2 to 3 then to 4
x_poly = poly_reg.fit_transform(x)#creating polynomial features
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)#used to fit it into a linear model

#visualizing the linear regresson results
plt.scatter(x, y, color= 'red')
plt.plot(x, lin_reg.predict(x), color='blue')
plt.title('truth ot bluff (linear regression')
plt.xlabel('position level')
plt.ylabel('Salary')
plt.show()

#visualizing polynomial regression results
x_grid = np.arange(min(x), max(x), 0.1)#reshape the grid to change by 0.1
x_grid = x_grid.reshape(len(x_grid), 1)#make the values a vector
plt.scatter(x, y, color= 'red')
plt.plot(x, lin_reg_2.predict(poly_reg.fit_transform(x)), color='blue')
plt.title('truth ot bluff (linear regression')
plt.xlabel('position level')
plt.ylabel('Salary')
plt.show()

#Predicting a new salary with linear 
lin_reg.predict(np.array([6.5]).reshape(1, 1))#reshapes to a 2D array

#Predict new salary with polynomial regression
n=lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))





