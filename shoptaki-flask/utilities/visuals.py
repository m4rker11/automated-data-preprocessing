import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

def CorrelationMatrixPlot(df):
    '''
    Takes a dataframe and plots a correlation matrix.
    '''
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.matshow(corr)
    return fig

def PlotMostCorrelated(df,target):
    """
    Finds three most correlated columns with target coolumn and plots them against target.
    """
    corr = df.corr()
    corr = corr.loc[target,:]
    corr = corr.sort_values(ascending=False)
    corr = corr.drop(target)
    corr = corr.head(3)
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.scatter(df[target],df[corr.index[0]],color='red')
    ax.scatter(df[target],df[corr.index[1]],color='blue')
    ax.scatter(df[target],df[corr.index[2]],color='green')
    ax.set_xlabel(target)
    ax.set_ylabel("3 Most Correlated With Target")
    ax.legend(corr.index)
    plt.show()

def PlotHistogram(df,target,bins=15):
    """
    Plots a histogram of target column.
    """
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.hist(df[target],bins)
    ax.set_xlabel(target)
    ax.set_ylabel("Frequency")
    plt.show()

