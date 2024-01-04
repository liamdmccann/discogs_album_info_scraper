#%%
import discogs_client
d = discogs_client.Client('my_user_agent/1.0', user_token='ZNjSMtuHsPmPqpByRPSWzAFLRbGaVZdTYsUYbmLH')
import csv
import pandas as pd
import time
from PIL import Image
from datetime import datetime, date
today = date.today().strftime('%Y-%m-%d')
print(today)
#%%
releases_DF = pd.read_csv('list of release IDs.csv')
releases_DF = releases_DF.sort_values("Release ID", ascending=True)
print (releases_DF)
release_list = releases_DF['Release ID'].tolist()
print(release_list)

release = d.release(1293022)
print(release.title)
artists = release.artists
#%%
record_list = []

for album in release_list:
    album = d.release(album)
    release_ID = album.id
    album_name = (album.title)
    year = (album.year)
    artist_name = (album.artists[0].name)
    label = album.labels[0].name
    record_data = (release_ID, year, artist_name, album_name, label)
#    cover_art = album.images[0]
    print(
            record_data
            )
    record_list.append(record_data)
    time.sleep(1)


records_DF = pd.DataFrame(record_list, columns=['Release ID', 'Album', 'Year', 'Artist Name', 'Label'])
print(records_DF)

records_DF.to_csv(today + ' - records_output.csv', encoding='utf-8')
# for album in releases_DF:
#     get_album_information = get_album_information(album)
#     album_info = get_album_information
#     print(album_info)
# #    print (year, album_name, artist_name, label)
#     time.sleep(1)
