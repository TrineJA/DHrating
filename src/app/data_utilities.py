import pandas as pd
import numpy as np

def split_TAUD_TACI(df:pd.DataFrame)->pd.DataFrame:
    # get Windward/leeward ratings and offshore rating
    mask_wl = df.columns.str.contains('TAUD|BoatKey')
    mask_circle = df.columns.str.contains('TACI|BoatKey')
    df_wl = df.loc[:,mask_wl].copy()
    df_wl.sort_values('3-9ms_TAUDM', ascending=False, inplace=True)
    df_circle = df.loc[:,mask_circle].copy()
    df_circle.sort_values('3-9ms_TACIM', ascending=False, inplace=True)
    return df_wl, df_circle


def wide_to_long(df_wide:pd.DataFrame)->pd.DataFrame:
    df_long = pd.melt(df_wide, id_vars=['BoatKey'], var_name='metric', value_name='value')
    return df_long


def get_rating_columns(df:pd.DataFrame)->list:
    # get columns to diff
    mask = df.columns.str.contains('TAUD|TACI')
    rating_columns = df.columns[mask]
    return rating_columns


def my_funky_formatter(x: float)->str:
    # converts a float in seconds to a string with minute/second format
    min_part_signed = int(np.trunc(x/60))

    if min_part_signed == 0:
        output_string = str(round(x, 1)) + 's'
    else:
        sec_part_abs = round(abs(x - (min_part_signed*60)),1)
        output_string = str(min_part_signed) + 'min ' + str(sec_part_abs) + 's'

    return output_string
