import pandas as pd
import numpy as np

# def load_csv(filePath, missing_headers=False):
#     """Read data as csv and return as pandas data frame."""

#     if missing_headers:
#         data = pd.read_csv(filePath, header=None)
#     else:
#         data = pd.read_csv(filePath, header=0)

#     # make shape of data frame global
#     global rows, cols
#     rows, cols = data.shape

#     return data

def autoconverter(file, filename):
    # if json convert to csv
    ext = filename.split('.')[-1]
    if ext in ['json', 'csv', 'xlsx', 'xls', 'pickle', 'sql']:
        if filename.endswith('.json'):
            df = pd.read_json(file)
        elif filename.endswith('.sql'):
            df = pd.read_sql(file)
        elif filename.endswith('.csv'):
            df = pd.read_csv(file)
        elif filename.endswith('.xlsx'):
            df = pd.read_excel(file)
        elif filename.endswith('.xls'):
            df = pd.read_excel(file)
        elif filename.endswith('.pickle'):
            df = pd.read_pickle(file)
        return df
    else:
        return pd.DataFrame()
    
    

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
    One hot encode categorical variables except datetimecolumns.
    Done Last
    """
    df = pd.get_dummies(df)
    return df


def remove_outliers(df):
    """
    Remove outliers from the data. 

    """
    for col in df.columns:
        if df[col].dtype == 'float64' or df[col].dtype == 'int64':
            df[col] = df[col].clip(lower=df[col].quantile(0.05), upper=df[col].quantile(0.95))
    return df
   


def delete_constant_columns(df):
    """
    Delete constant columns.
    """
    df = df.loc[:, (df != df.iloc[0]).any()]
    return df
def combine_first_last_name(df):
    """
    Combine first and last name if df has those columns.
    """
    if 'first_name' in df.columns and 'last_name' in df.columns:
        df['full_name'] = df['first_name'] + ' ' + df['last_name']
        df.drop(['first_name', 'last_name'], axis=1, inplace=True)
    return df

def drop_useless_columns(df): #like name and ID and email
    """
    if more than 95 percent of the values aren't repeating delete column.
    """
    for col in df.columns:  
        if df[col].nunique() > 0.95 * len(df):
            df.drop(col, axis=1, inplace=True)
    return df

def normalize(df):
    """
    Normalize data.
    """
    for col in df.columns:
        if df[col].dtype == 'float64':
            df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    return df

def check_if_dateTime(df):
    """
    Check if the data is dateTime.
    """
    for col in df.columns:
        if df[col].dtype == 'object':
            try:
                df[col] = pd.to_datetime(df[col], infer_datetime_format=True)
            except:
                pass
    
    
    
    dateTimeColumns = []
    for col in df.columns:
        if df[col].dtype == 'datetime64[ns]':
            dateTimeColumns.append(col)
    return df, dateTimeColumns
    