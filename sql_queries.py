# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays;"
user_table_drop = "DROP table IF EXISTS  users;"
song_table_drop ="DROP table IF EXISTS songs;"
artist_table_drop = "DROP table IF EXISTS artists;"
time_table_drop = "DROP table IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
songplay_id  SERIAL NOT NULL, 
start_time date, 
user_id text, 
level varchar , 
song_id text, 
artist_id text, 
session_id text, 
location text, 
user_agent text,
PRIMARY KEY(songplay_id)

);

""")

user_table_create = ("""

CREATE TABLE IF NOT EXISTS users (
user_id text NOT NULL, 
first_name varchar,
last_name varchar, 
gender varchar, 
level varchar

);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
song_id text NOT NULL,
title varchar,
artist_id text, 
year int,
duration decimal
);
""")

artist_table_create = ("""

CREATE TABLE IF NOT EXISTS artists (
artist_id text, 
name varchar, 
location varchar, 
latitude decimal, 
longitude decimal

);

""")

time_table_create = ("""

CREATE TABLE IF NOT EXISTS time (
start_time timestamp NOT NULL, 
hour int, 
day int, 
week int,
month int, 
year int, 
weekday int
);

""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (songplay_id,start_time,user_id,level,song_id,artist_id,session_id,location,user_agent) \
     VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s) 
     ON CONFLICT(songplay_id) 
     DO UPDATE SET start_time= EXCLUDE.start_time;
""")

user_table_insert = ("""
INSERT INTO users(user_id,first_name,last_name,gender,level)\
                 VALUES (%s, %s, %s, %s,%s)
""")

song_table_insert = ("""
INSERT INTO songs (song_id,title,artist_id,year,duration)\
                 VALUES (%s, %s, %s, %s,%s)
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)\
                 VALUES (%s, %s, %s, %s, %s)

""")


time_table_insert = ("""
INSERT INTO time (start_time,hour,day,week,month,year,weekday)\
                 VALUES (%s, %s, %s, %s, %s, %s, %s)

""")

# FIND SONGS

song_select = ("""
    SELECT songs.song_id, songs.artist_id FROM songs JOIN artists ON songs.artist_id =artists.artist_id
    where songs.title= %s and artists.name= %s and songs.duration= %s ;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]