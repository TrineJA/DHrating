import pandas as pd
import pickle
import glob

## configs
myBoat = 'ITALIA 9.98 / DEN-998'


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


# read certificate data
all_dicts = sorted(glob.glob('data/*.pickle'))
# open latest pickle available
with open(all_dicts[-1], 'rb') as handle:
    dict_final = pickle.load(handle)

# transform to dataframe
df_cert = pd.DataFrame.from_dict(dict_final, orient='index')

# add boat identifier
df_cert['BoatKey'] = df_cert.Class + ' / ' + df_cert.SailNo

# add windspeed information to column names
df_cert.rename(columns={"TAUDL":"0-4ms_TAUDL",
                        "TAUDM":"3-9ms_TAUDM",
                        "TAUDH":"8-ms_TAUDH",
                        "TACIL":"0-4ms_TACIL",
                        "TACIM":"3-9ms_TACIM",
                        "TACIH":"8-ms_TACIH"},
               inplace=True)

# calculate diff from our boat
diff = df_cert.copy()
# get columns to diff
mask = df_cert.columns.str.contains('TAUD|TACI')
ws_cols = df_cert.columns[mask]
# do the subtraction
diff[ws_cols] = diff[ws_cols] - diff.loc[diff.BoatKey == myBoat, ws_cols].values.squeeze()

## split data in TACI and TAUD
df_wl, df_circle = split_TAUD_TACI(df_cert)
df_wl_diff, df_circle_diff = split_TAUD_TACI(diff)

# make format long (better for plotting)
df_wl = wide_to_long(df_wl)
df_circle = wide_to_long(df_circle)
df_wl_diff = wide_to_long(df_wl_diff)
df_circle_diff = wide_to_long(df_circle_diff)



