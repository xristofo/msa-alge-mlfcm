# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 23:25:37 2020

@author: andreas
"""

# importing the required module 
import matplotlib.pyplot as plt 

# x axis values 
x=[1,2,3,4,5,6,7,8,9,10,11,12]
y1 = [2,4,4,11,5,7,13,3,9,9,8,9] 
# corresponding y axis values 
y2 = [2,6,10,21,26,33,46,49,58,67,75,84] 

# plotting the points 
plt.plot(x, y2, label='daily') 
plt.plot(x, y1, label='total cases') 

# naming the x axis 
plt.xlabel('') 
# naming the y axis 
plt.ylabel('') 

# giving a title to my graph 
plt.title('') 
plt.legend() 

# function to show the plot 
plt.show() 
