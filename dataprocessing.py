import pandas as pd

def convert_to_numeric(df):
    
    df['duration'] = df['duration'].astype(str).str.extract(r'(\d+)')
    df['duration'] = df['duration'].astype('Int16')

    df['calories'] = df['calories'].astype(str).str.extract(r'(\d+)')
    df['calories'] = df['calories'].astype('Int16')
    return df

def data_standardatization(df):
    
    mapping = {
        'walk': 'walking',
        'swimm': 'swimming',
        'swim': 'swimming'
    }
    df['activity'] = df['activity'].astype(object).replace(mapping).astype("category")
    return df

def deduplicated_data(df):
    df.drop_duplicates(keep='first', inplace=True, ignore_index=False)
    df.dropna(inplace=True)
    return df

def prepare_data(df):
    return df.pipe(convert_to_numeric).pipe(data_standardatization).pipe(deduplicated_data)
    



