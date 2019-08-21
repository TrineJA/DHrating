from bs4 import BeautifulSoup
import glob
import re
import pickle
import time


def main():
    # initialize
    dict_final = {}

    for i, filename in enumerate(glob.glob('data/certificates/*')):
        soup = BeautifulSoup(open(filename,'r'), "html.parser")

        # check if certificate is valid
        if soup.find(class_='ikkegyldig') is not None:
            print(f'Skipping certificate {filename} - certificate is not valid')
            continue
        else:
            print((f'Reading certificate {filename}'))

        cert2 = soup.find_all('b')

        # get ratings (index 2 to 10 after 'Ratings')
        for idx in range(0,len(cert2)):
            if cert2[idx].get_text() == 'Ratings':
                idx_rating = idx

        ratings_keys = ['GPH','TCC','TACIL','TACIM','TACIH','TAUDL','TAUDM','TAUDH']
        ratings_values = []
        for idx in range(idx_rating+2,idx_rating+10):
            ratings_values.append(float(cert2[idx].get_text().replace(',','.')))

        ratings = dict(zip(ratings_keys, ratings_values))

        # get metadata (always index 3 and 5)
        idxs = [3,5]
        metadata_keys = ['Class','SailNo']
        metadata_values = []
        for idx in idxs:
            # get data (replace `\xa0' (non-breaking space) with -
            metadata_values.append(cert2[idx].get_text().replace(u'\xa0', u'-'))

        metadata = dict(zip(metadata_keys, metadata_values))

        # collect all data
        certificate_id = re.split("/",filename)[-1]
        dict_final.update({certificate_id: dict(metadata,**ratings)})

    # write to pickle
    with open('data/'+str(int(time.time()))+'_dict_final.pickle', 'wb') as handle:
        pickle.dump(dict_final, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    main()
