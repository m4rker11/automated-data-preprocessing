import pandas as pd
import numpy as np

def load_csv(filePath, missing_headers=False):
    """Read data as csv and return as pandas data frame."""

    if missing_headers:
        data = pd.read_csv(filePath, header=None)
    else:
        data = pd.read_csv(filePath, header=0)

    # make shape of data frame global
    global rows, cols
    rows, cols = data.shape

    return data

def fill_empty_with_nan(df):
    """
    Fill empty values with NaN.
    """
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col].fillna(np.nan, inplace=True)
    return df

def drop_missing_data(df):
    """
    if more than 2 fields are missing drop the row.
    if more than half of the fields are missing drop the column.
    """
    df.dropna(axis=0, thresh=2, inplace=True)
    df.dropna(axis=1, thresh=0.5, inplace=True)

    return df

def replace_missing_data(df):
    """
    Replace missing numerical data with the median for each column.

    """
    for col in df.columns:
        if df[col].dtype == 'float64' or df[col].dtype == 'int64':
            df[col].fillna(df[col].median(), inplace=True)
    return df

def one_hot_encode(df):
    """
    One hot encode categorical variables.

    """
    df = pd.get_dummies(df)
    return df


def remove_outliers(df):
    """
    Remove outliers from the data.

    """
    for col in df.columns:
        if df[col].dtype == 'float64' or df[col].dtype == 'int64':
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - (iqr * 1.5)
            upper_bound = q3 + (iqr * 1.5)
            df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]
    return df

def normalize(df):
    """
    Normalize the data.
    """
    for col in df.columns:
        if df[col].dtype == 'float64' or df[col].dtype == 'int64':
            df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    return df

def preprocess_data(df):
    """
    Preprocess the data.
    """
    df = fill_empty_with_nan(df)
    df = drop_missing_data(df)
    df = replace_missing_data(df)
    df = one_hot_encode(df)
    df = remove_outliers(df)
    df = normalize(df)
    return df
