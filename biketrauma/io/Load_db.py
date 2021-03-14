import pandas as pd
from download import download
# import biketrauma
from biketrauma.io import path_target,url_db


class Load_db:
  def __init__(self, url=url_db, target_name=path_target):
    download(url, target_name, replace=False)
  
  @staticmethod
  def save_as_df():
    df_bikes = pd.read_csv(path_target, na_values="", low_memory=False, converters={'data': str, 'heure': str})
    return df_bikes