import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

## ACQUISITION:

def acquire_big_5_data():
    #Acquiring Big 5 Data from CSV of user responses:
    df = pd.read_csv('big_5_data.csv', sep = '\t')
    return df

## PREPARATION:

def prep_big_5_data(df):
    #Creating list to drop columns that contain time to click answers, as well as screen size and latitude/longitude guesses:
    drop_columns = ['EXT1_E', 'EXT2_E', 'EXT3_E', 'EXT4_E', 'EXT5_E', 'EXT6_E', 'EXT7_E', 'EXT8_E', 'EXT9_E', 'EXT10_E', 'EST1_E', 'EST2_E', 'EST3_E', 'EST4_E', 'EST5_E', 'EST6_E', 'EST7_E', 'EST8_E', 'EST9_E', 'EST10_E', 'AGR1_E', 'AGR2_E', 'AGR3_E', 'AGR4_E', 'AGR5_E', 'AGR6_E', 'AGR7_E', 'AGR8_E', 'AGR9_E', 'AGR10_E', 'CSN1_E', 'CSN2_E', 'CSN3_E', 'CSN4_E', 'CSN5_E', 'CSN6_E', 'CSN7_E', 'CSN8_E', 'CSN9_E', 'CSN10_E', 'OPN1_E', 'OPN2_E', 'OPN3_E', 'OPN4_E', 'OPN5_E', 'OPN6_E', 'OPN7_E', 'OPN8_E', 'OPN9_E', 'OPN10_E', 'screenw', 'screenh', 'lat_appx_lots_of_err', 'long_appx_lots_of_err', 'dateload', 'introelapse', 'testelapse', 'endelapse']
    #Dropping Unneeded Columns:
    df = df.drop(columns=drop_columns)
    #Converting all '0.0' values to null:
    df = df.replace(0.0, np.nan)
    #Dropping Null Values:
    df = df.dropna()
    # Dropping rows that come from non-unique IP addresses for the sake of cleanliness:
    df = df.drop(df[df.IPC > 1].index)
    #Dropping 'IPC' column after dropping non-unique IP rows:
    df = df.drop(columns = 'IPC')
    return df

def split_big_5_data(df):
    # Creating test set as 20% of original data: 
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    # Creating train and validate sets: 
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)
    return train, validate, test