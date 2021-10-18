import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
popu = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, popu )# Plots a line
#plt.scatter(year, popu)#Plots the points
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World population projections')
plt.yticks([0,2,4,6,8,10],
           ['0','2B','4B','6B','8B','10B'])#Changing the scale to be in intervals of 2 with new names
plt.show()

#Histogram
values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]
plt.hist(values, bins=3)
#plt.show()