import pandas as pd
import numpy as np

def load_data(file_path:str):
    df = pd.read_csv(file_path)
    return df





def cleaned_data(DataFrame):
    # create a copy of data
    df_copy = DataFrame.copy()
    df_copy = df_copy.drop(df_copy.index[10472])
    # convert the columns Size to right data type
    df_copy['Size'] = df_copy['Size'].str.replace('M', '000')
    df_copy['Size'] = df_copy['Size'].str.replace('k', '')
    df_copy['Size'] = df_copy['Size'].replace('Varies with device', np.nan)
    df_copy['Size'] = df_copy['Size'].astype(float)
    # clean the price columns and convert it into an float data type
    df_copy['Price'] = [i.replace('$', '') for i in df_copy['Price']]
    df_copy['Price'] = df_copy['Price'].astype(float)
    # the same things for Install columns
    df_copy['Installs'] = [i.replace('+', '').replace(',', '') for i in df_copy['Installs']]
    df_copy['Installs'] = df_copy['Installs'].astype(int)
    # convert the date columns into date data type
    df_copy['Last Updated'] = pd.to_datetime(df_copy['Last Updated'])
    # create new columns
    df_copy['Day'] = df_copy['Last Updated'].dt.day
    df_copy['Month'] = df_copy['Last Updated'].dt.month
    df_copy['Year'] = df_copy['Last Updated'].dt.year
    return df_copy


def save_data_to_csv(dt_cleaned, file_path:str):
    dt_cleaned.to_csv(f"{file_path}")
                 
