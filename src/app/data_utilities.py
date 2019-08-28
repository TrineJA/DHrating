import pandas as pd

def split_TAUD_TACI(df:pd.DataFrame)->pd.DataFrame:
    # get Windward/leeward ratings and offshore rating
    mask_wl = df.columns.str.contains('TAUD|BoatKey')
    mask_circle = df.columns.str.contains('TACI|BoatKey')
    df_wl = df.loc[:,mask_wl]
    df_circle = df.loc[:,mask_circle]
    return df_wl, df_circle


def wide_to_long(df_wide:pd.DataFrame)->pd.DataFrame:
    df_long = pd.melt(df_wide, id_vars=['BoatKey'], var_name='metric', value_name='value')
    return df_long
