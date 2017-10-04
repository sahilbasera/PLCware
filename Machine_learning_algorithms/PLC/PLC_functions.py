import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


"""
This python file contains all the functions

"""



#This function trains the ML model for the temperature probability 

            
def temp():
    data = pd.read_csv('tempDataset.csv')

    X = data[['Temperature']]   
    Y = data['Probability']

    X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size = 0.2 , random_state = 2)

    reg1 = RandomForestRegressor(n_estimators = 15 , min_samples_split = 1)
    reg1 = reg1.fit(X_train , Y_train)
    return reg1


# This function test the ML model for an input temperature given by the user 


def temppredict(x):
     reg = temp()
     abc = reg.predict(x)
     return abc


# This function trains the ML model for the input voltage probability 

    
def voltage() :
    data = pd.read_csv('IVDataset.csv')

    X = data[['IV']]
    Y = data['Probability']

    X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size = 0.2 , random_state = 2)

    reg =  RandomForestRegressor(n_estimators = 15 , min_samples_split = 1)
    reg = reg.fit(X_train , Y_train)
    return reg


# This function tests the ML model for an input temperature given by the user 
 

def voltagepredict(x):
     reg = voltage()
     abc = reg.predict(x)
     return abc 

