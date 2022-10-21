import os
from dotenv import load_dotenv, find_dotenv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
# Set plot style

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

INPUT_DATAFRAME = os.environ.get("INPUT_DATAPATH")

class DataPreProcess():
    """
    A class for importing and preprocessing of our dataset
    """
    OUTPUT_DATAFRAME = os.environ.get("PROCESSED_DATAPATH")
    def __init__(self, columns: list = None, scaler = None):
        """
        ----------
        Initializes DataPreProcess Class
        ----------
        Parameters
        ----------
        path : str
            full path to the data source.
        columns : list
            columns that are not needed and need to
            be dropped from the data."""
        self._columns = columns
        self._scaler = scaler
    def import_data(self, path: str = None, columns: list = None):
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
    def balanced_data(data: pd.DataFrame = None):
        """
        function to split our datasets and 
        correct the imbalances of classes o
        bserved in the datasets"""
        df = data.values
        X, y = df[:,:-1], df[:,-1]
        labelencoder = LabelEncoder()
        y = LabelEncoder().fit_transform(y)
        oversample = SMOTE()
        X, y = oversample.fit_resample(X, y)
        scaler = MinMaxScaler()
        X = scaler.fit_transform(X.to_numpy())
        counter = Counter(y)
        for key,value in counter.items():
            per = value / len(y) * 100
            print('Class=%d, n=%d (%.3f%%)' % (key, value, per))
        return X, y
    @classmethod    
    def export_data(cls, X_train, y_train, out_path):
        """
        """
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        out_path = os.path.join(cls.OUTPUT_DATAFRAME, out_path)
        df = pd.DataFrame ({'X':X_train,'Y':y_train})
        return df.to_csv(out_path)
