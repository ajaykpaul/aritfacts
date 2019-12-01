import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
from pptx.dml import color
import os    

"""
  A very simple linear regression with least square technique and error function R**2

"""

def main():
    print(os.getcwd()) 
    data = pd.read_csv("datasets/pair1.csv")
    x = data['X'].values
    y = data['Y'].values
    mean_x, mean_y = np.mean(x), np.mean(y)
    
    num_ = 0
    den_ = 0
    for i in range(len(x)):
        num_ += (x[i] - mean_x) * (y[i] - mean_y)
        den_ += (x[i] - mean_y) ** 2
        
    m = num_ / den_
    c = mean_y - m * mean_x
    
    max_x = np.max(x) + 100
    min_x = np.min(x) - 100
   
    x_pridict = np.linspace(min_x, max_x, 1000)
    y_predict = m * x_pridict + c
    
    plt.scatter(x, y, c='#ef5423', label="scattered plot")
    plt.plot(x_pridict, y_predict, color='#58b970', label="regression line")
    plt.xlabel("X-Axis")
    plt.ylabel("X-Axis")
    plt.legend()
    plt.show()
    
    ss_t = 0
    ss_r = 0
    
    l = len(x)
    for i in range(l):
        y_predict = c + m * x[i]
        ss_t += (y[i] - mean_y) ** 2
        ss_r += (y[i] - y_predict) ** 2

    r2 = 1 - (ss_r / ss_t)
    print(r2)
    
    
if __name__ == "__main__": 
    main()
