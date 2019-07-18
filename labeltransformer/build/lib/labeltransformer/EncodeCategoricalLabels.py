from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np

class EncodeCategoricalLabels(BaseEstimator, TransformerMixin):
    def __init__(self):
            self.dict = {}
    def fit(self, vals, Y):
        columns = df.columns.values
        for column in columns:
            text_digit_vals = {}
            def convert_to_int(val):
                return text_digit_vals[val]
            if df[column].dtype != np.int64 and df[column].dtype != np.float64:
                column_contents = df[column].values.tolist()
                unique_elements = set(column_contents)
                x = 0
                for unique in unique_elements:
                    if unique not in text_digit_vals:
                        text_digit_vals[unique] = x
                        x = x + 1
                df[column] = list(map(convert_to_int,df[column]))
        self.dict = text_digit_vals
        return df

    def convertToInt(self,val):
        return self.dict[val]

    def fit_transform(self, df,Y=None):
        columns = df.columns.values
        text_digit_vals = {}
        for column in columns:
            def convert_to_int(val):
                return text_digit_vals[val]
            if df[column].dtype != np.int64 and df[column].dtype != np.float64:
                column_contents = df[column].values.tolist()
                unique_elements = set(column_contents)
                x = 0
                for unique in unique_elements:
                    if unique not in text_digit_vals:
                        text_digit_vals[unique] = x
                        x = x + 1
                df[column] = list(map(convert_to_int,df[column]))
        self.dict = text_digit_vals
        return df

    def transform(self, vals,Y=None):
        columns = vals.columns.values
        for column in columns:
            if vals[column].dtype != np.int64 and vals[column].dtype != np.float64:
                vals[column] = list(map(self.convertToInt,vals[column]))
        return vals
