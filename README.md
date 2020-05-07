# Project: Data Modeling with Postgres

### Project Description
In this project, we implemented data modeling with Postgres and build an ETL pipeline using Python. To complete the project, we will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

### Dataset 
 - Song Dataset
   - song_data/A/B/C/TRABCEI128F424C983.json
   ```
   {"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
   ```
 - Log Dataset
   - log_data/2018/11/2018-11-12-events.json

### File description 
1. test.ipynb displays the first few rows of each table to let you check your database.

2. create_tables.py drops and creates your tables. .

3. etl.ipynb reads and processes a single file from song_data and log_data and loads the data into tables. This notebook contains detailed instructions on the ETL process for each of the tables.

4. etl.py reads and processes files from song_data and log_data and loads them into your tables.

5. sql_queries.py contains all your sql queries, and is imported into the last three files above.

### Acknolegdement
[UDACITY](https://www.udacity.com/)

