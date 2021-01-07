def scrap_table_wikipedia (url, df_number=0):
    '''
    Uses requests to get source code from url.
    Then pandas.read_html to get all tables as pandas dataframes.
    Returns selected dataframe
    Parameters:
    * url <str> : url to take dataframes from.
    * df_number <int> : Number of dataframe to collect from the dataframes in the url.
    * index_column <none or int> : if specified, defines column at specified index 
    as the dataframe index 
    '''

    import requests
    import pandas as pd

    # Get html content as a string
    try:
        string = requests.get(url).text
    except:
        return "Did you enter a valid url string? Could not get info from requested url."

    # Use pandas.read_html to get the list of dataframes from previous string
    try:
        dfs = pd.read_html(string)
    except:
        return "Are there tables in the specified url? \
            Could not use pandas.read_html to get dataframes from source code in url"

    

    # Index column optional functionality 
    if index_column:
        df = dfs[index_column].set_index(dfs[index_column].columns[0], drop=True).sort_index()
        else: df = dfs[0] # default: get 1st dataframe

    return df


    
