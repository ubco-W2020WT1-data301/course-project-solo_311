import pandas as pd
def load_and_process(url_or_path_to_csv_file):
    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_excel(url_or_path_to_csv_file)
        .dropna()
        .reset_index()
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
        .assign(year=pd.to_datetime(df1['year'], errors = 'coerce').dt.year)
        .dropna()
        .reset_index()
        .drop(columns=['index'])
        .drop(columns=['level_0'])
        
      )
    df3 = (
    df2.assign(year = df2['year'].astype(int))
    .query('year < 2021')
    .drop(columns=['GeoLocation'])

    )


    # Make sure to return the latest dataframe

    return df3