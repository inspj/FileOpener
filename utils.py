import pandas as pd

def info_reader():
    file = pd.read_csv('C:\\x')
    file_df = pd.DataFrame(file)
    
    studies = [str(x) for x in list(file_df["STUDY NAME"])]
    folders = list(file_df.columns)[1:]

    return studies, folders

