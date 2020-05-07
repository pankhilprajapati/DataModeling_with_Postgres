# DROP TABLES

songplay_table_drop = "drop table IF EXISTS songplays;"
user_table_drop = "drop table IF EXISTS users;"
song_table_drop = "drop table IF EXISTS songs;"
artist_table_drop = "drop table IF EXISTS artists;"
time_table_drop = "drop table IF EXISTS times;"

# CREATE TABLES

songplay_table_create =("""
CREATE TABLE IF NOT EXISTS songplays
                         (songplay_id serial NOT NULL PRIMARY KEY,
                         timestamp bigint NOT NULL,
                         user_id varchar NOT NULL,
                         level varchar,
                         song_id varchar,
                         article_id varchar,
                         session_id varchar NOT NULL,
                         location varchar,
                         user_agent varchar);
""")

user_table_create =("""
CREATE TABLE IF NOT EXISTS users 
                        (user_id varchar NOT NULL PRIMARY KEY,
                        first_name varchar,
                        last_name varchar,
                        gender varchar NOT NULL,
                        level varchar NOT NULL)
""") 

song_table_create =("""
CREATE TABLE IF NOT EXISTS songs 
                     (song_id varchar NOT NULL PRIMARY KEY 
                     ,title varchar 
                     ,artist_id varchar NOT NULL 
                     , year int
                     , duration float)
""")

artist_table_create =("""
CREATE TABLE IF NOT EXISTS artists 
                       (artist_id varchar NOT NULL PRIMARY KEY 
                        ,artist_name varchar 
                        ,artist_location varchar 
                        ,artist_latitude float 
                        ,artist_longitude float)
""")

time_table_create =("""
CREATE TABLE IF NOT EXISTS times
                     (timestamp bigint NOT NULL PRIMARY KEY
                      ,hour int NOT NULL 
                      ,day int NOT NULL 
                      ,week int NOT NULL 
                      ,month int NOT NULL 
                      ,year int NOT NULL 
                      ,weekday int NOT NULL)
""")

# INSERT RECORDS

songplay_table_insert =("""
INSERT INTO songplays (timestamp,user_id,level,song_id,article_id,session_id,location,user_agent) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
""")
user_table_insert = ("""
INSERT INTO users (user_id,first_name, last_name,gender,level) VALUES (%s,%s,%s,%s,%s)
ON CONFLICT (user_id) DO UPDATE SET level=excluded.level;
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title,artist_id, year, duration) VALUES (%s,%s,%s,%s,%s)
ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, artist_name, artist_location,artist_latitude, artist_longitude) VALUES (%s,%s,%s,%s,%s)
ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO times (timestamp, hour, day, week, month, year, weekday) VALUES (%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT (timestamp) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT songs.song_id, artists.artist_id 
      FROM songs JOIN artists 
      ON songs.artist_id = artists.artist_id 
      WHERE songs.title = %s
            AND artists.artist_name = %s
            AND songs.duration = %s
      GROUP BY
        songs.song_id,
        artists.artist_id

""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]