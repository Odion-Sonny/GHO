import csv
import duckdb

# Define the input CSV file paths
users_file = 'user_attributes.csv'
events_file = 'user_event.csv'

# Define the output file paths
users_output_file = 'users_transformed.csv'
events_output_file = 'events_transformed.csv'


# Transform the users CSV file
with open(users_file, 'r') as infile, open(users_output_file, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ['user_id', 'name', 'age', 'gender', 'location', 'signup_date', 'subscription_plan', 'device_type']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
        row['user_id'] = int(row['user_id'])
        row['age'] = int(row['age'])
        writer.writerow(row)

# Transform the events CSV file
with open(events_file, 'r') as infile, open(events_output_file, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ['user_id', 'event_name', 'time_stamp']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
        row['user_id'] = int(row['user_id'])
        writer.writerow(row)

# Load the transformed data into DuckDB
conn = duckdb.connect(database='my_db.duckdb')
conn.execute(f"CREATE TABLE users(user_id INTEGER PRIMARY KEY, name VARCHAR, age INTEGER, gender VARCHAR, location VARCHAR, signup_date DATE, subscription_plan VARCHAR, device_type VARCHAR);")
conn.execute(f"COPY users FROM '{users_output_file}' DELIMITER ',' CSV HEADER;")
conn.execute(f"CREATE TABLE user_events(user_id INTEGER REFERENCES users(user_id), event_name VARCHAR, timestamp TIMESTAMP);")
conn.execute(f"COPY user_events FROM '{events_output_file}' DELIMITER ',' CSV HEADER;")


# conn.execute(f"SELECT DISTINCT users.user_id FROM users INNER JOIN user_events ON users.user_id = user_events.user_id WHERE location = 'California' AND event_name = 'LOGIN';")

# Close the connection
conn.close()
# SELECT DISTINCT users.user_id 
# FROM users INNER JOIN user_events 
# ON users.user_id = user_events.user_id 
# WHERE location = 'California' 
# AND event_name = 'LOGIN';

# SELECT user_id FROM user_events
# WHERE event_name = 'LOGIN'
# AND user_id IN (SELECT user_id FROM users WHERE location = 'California');

# SELECT DISTINCT users.user_id FROM users INNER JOIN user_events ON users.user_id = user_events.user_id WHERE users.location = 'California' AND user_events.event_name = 'LOGIN';