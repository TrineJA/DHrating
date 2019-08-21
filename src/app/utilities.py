import pandas as pd
import pickle
import glob


def load_data() -> pd.DataFrame:
    # read data
    all_dicts = sorted(glob.glob('data/*.pickle'))

    # open latest pickle available
    with open(all_dicts[-1], 'rb') as handle:
        dict_final = pickle.load(handle)

    # transform to dataframe
    df = pd.DataFrame.from_dict(dict_final, orient='index')

    # add windspeed info to DataFrame
    df['valid_windspeed_kn'] = 0

    return df


