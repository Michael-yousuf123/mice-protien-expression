import os
from dotenv import load_dotenv, find_dotenv
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Set plot style
sns.set(color_codes=True)

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

INPUT_DATAFRAME = os.environ.get("INPUT_DATA")

class DataPreProcess():
    pass 
def __init__(self, ):
    pass
def import_data(path: str = None, columns: list = None):
    """
    Function to import a dataset into 
    the working environment
    --------------------------------
    Parameter
    ----------
    path : str
    Usually a string with the path of the data
    --------------------------------
    Returns
    -------
    data : dataframe
    Returns a pandas dataframe
     """
    data = pd.read_excel(path)
    if columns:
        data = data.drop(columns, axis = 1)
    return data

def null_test(data: pd.DataFrame=None):
    """ 
    A function to fill the Null values with
    the mean of our dataset
    ---------
    Parameters
    param: pandas dataframe
    ----------
    Returns
    a dataframe cleaned of missing values
    -----------
    """
    if data.isnull().any().any():
        data.fillna(data.mean(), inplace=True)
    else:
        print("No missing values encountered")  
    return data
def balanced_data(data: pd.DataFrame ):
    """
    function to split our datasets and 
    correct the imbalances of classes o
    bserved in the datasets"""
    from collections import Counter
    from imblearn.over_sampling import SMOTE
    from sklearn.preprocessing import LabelEncoder
    labelencoder = LabelEncoder()
    df = data.values
    X, y = df[:,:-1], df[:,-1]
    y = LabelEncoder().fit_transform(y)
    oversample = SMOTE()
    X, y = oversample.fit_resample(X, y)
    counter = Counter(y)
    for k,v in counter.items():
        per = v / len(y) * 100
        print('Class=%d, n=%d (%.3f%%)' % (k, v, per))
    # plot the distribution
    plt.bar(counter.keys(), counter.values())
    plt.show()