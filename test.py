#import numpy
import numpy as np

#Declaring our list
height = [1.78, 1.68, 1.55, 1.88, 1.69]
weight = [65.4, 59.2, 63.6, 75.8, 69.9]

np_height = np.array(height) #use the same data or they will be converted
np_weight = np.array(weight)

#Working the new formula
bmi = np_weight/np_height**2

#Printing results
print(bmi) 

#how lists work
final = height + weight
#print(final)

#how numpy arrays work
np_final = np_weight + np_height
#print(np_final)
#print(bmi>23)# Prints true or false if value is greater than 23
#print(bmi[bmi>23])# Prints the actual values greater than 23

#2D numpy array
np_2d = np.array([[1.78, 1.68, 1.55, 1.88, 1.69],
				[1.78, 1.68, 1.55, 1.88, 1.69]])

#print(np_2d)#shows the values
#print(np_2d.shape)# Looking at the dimensions
#print(np_2d)
#print(np_2d[0,3])#selecing values
#print(np_2d[:, 1:3]) #Select all rows but only he firs two columns
#print(np_2d[1,:]) #Select the first row and all columns
#print(np.mean(np_2d[1,:]))#printing the mean values, can use median,std, co-coeff
heights = np.round(np.random.normal(1.75, 0.20, 5000), 2)
print(heights)