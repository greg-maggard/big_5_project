import pandas as pd

def acquire_big_5_data():
    #Acquiring Big 5 Data from CSV of user responses:
    df = pd.read_csv('big_5_data.csv', sep = '\t')
    return df