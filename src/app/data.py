import pandas as pd
import pickle
import glob
from data_utilities import split_TAUD_TACI, get_rating_columns

## configs
myBoat = 'ITALIA 9.98 / DEN-998'

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
df_cert_diff = df_cert.copy()
# get columns to diff
ws_cols = get_rating_columns(df_cert_diff)
# do the subtraction
df_cert_diff[ws_cols] = round(df_cert_diff[ws_cols] - df_cert_diff.loc[df_cert_diff.BoatKey == myBoat, ws_cols].values.squeeze(),1)

## split data in TACI and TAUD
df_wl, df_circle = split_TAUD_TACI(df_cert)
df_wl_diff, df_circle_diff = split_TAUD_TACI(df_cert_diff)