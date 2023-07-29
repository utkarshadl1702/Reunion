# Load the data and perform transformations to simply the data and store it a normalized manner into smaller tables which are easier to analyze

import json
import pandas as pd
import sqlite3

# Step 1: Load the JSON data
with open('nested_data.json') as f:
    data = json.load(f)

# Step 2: Normalize the data and create pandas DataFrames
# Extracting data for Orchestras
orchestras = pd.DataFrame(data['Orchestras']).transpose().reset_index()
orchestras.columns = ['orchestra_id', 'orchestra_name', 'country']

# Extracting data for Concerts
concerts_data = []
for orchestra_id, concerts in data['Concerts'].items():
    for concert in concerts:
        concerts_data.append([orchestra_id, concert['location'], concert['date']])
concerts = pd.DataFrame(concerts_data, columns=['orchestra_id', 'location', 'date'])

# Extracting data for Works
works_data = []
for concert_id, works in data['Works'].items():
    for work in works:
        works_data.append([concert_id, work['work_id'], work['work_name']])
works = pd.DataFrame(works_data, columns=['concert_id', 'work_id', 'work_name'])

# Extracting data for Artists
artists_data = []
for concert_id, artists in data['Artists'].items():
    for artist in artists:
        artists_data.append([concert_id, artist['artist_id'], artist['artist_name'], artist['instrument']])
artists = pd.DataFrame(artists_data, columns=['concert_id', 'artist_id', 'artist_name', 'instrument'])

# Step 3: Create a SQLite database and insert data into tables
conn = sqlite3.connect('orchestra_data.db')
cursor = conn.cursor()

# Create tables
orchestras.to_sql('Orchestras', conn, if_exists='replace', index=False)
concerts.to_sql('Concerts', conn, if_exists='replace', index=False)
works.to_sql('Works', conn, if_exists='replace', index=False)
artists.to_sql('Artists', conn, if_exists='replace', index=False)

# Commit changes and close the connection
conn.commit()
conn.close()
