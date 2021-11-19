
import argparse
import numpy as np
import pandas as pd
from utilities import *

def clean(args):
    """Load and clean user-supplied data."""

    print('CLEANING DATA....')
    # load data as a pandas data frame
    df = pd.read_csv(args.filePath, low_memory=False)

    # interpolate missing data values
    if args.interpolate or args.all:
        print('\tDetecting missing values...')
        df = fill_empty_with_nan(df)
        print('\tImputing missing values...')
        df = replace_missing_data(df)
        df = drop_missing_data(df)

    # detect and remove outliers
    if args.outliers or args.all:
        print('\tRemoving outliers...')
        df = remove_outliers(df)
        df = normalize(df)

    # one-hot encode the categorical variables
    

    # delete useless columns
    if args.all:
        print('\tDeleting useless columns...')
        df = combine_first_last_name(df)
        df = drop_useless_columns(df)
        df, date = check_if_dateTime(df)
    # save cleaned data file to same directory as uncleaned version
    

    if args.categorical or args.all:
        print('\tTransforming categorical data using one-hot encoding...')
        df = one_hot_encode(df)
    df.to_csv(args.filePath[:-4] + '_CLEANED.csv')
    print('DONE.')
    return df

def add_args(parser):
    """Add command line options for customized data preprocessing."""
    parser.add_argument('filePath', metavar='filePath', type=str, help='Path to uncleaned data file')
    parser.add_argument('-a', '--all', action='store_const', const='a')
    parser.add_argument('-c', '--categorical', action='store_const', const='c')
    parser.add_argument('-i', '--interpolate', action='store_const', const='i')
    parser.add_argument('-m', '--missing', action='store_const', const='m')
    parser.add_argument('-o', '--outliers', action='store_const', const='o')
    parser.add_argument('-v', '--version', action='version', version='v1.0.0')

def main():
    """Create command line argument parser and call clean for preprocessing."""
    parser = argparse.ArgumentParser()
    add_args(parser)
    args = parser.parse_args()
    print(args)
    df = clean(args) # clean data according to user-supplied options
    # CorrelationMatrixPlot(df)
if __name__ == '__main__':
    main()