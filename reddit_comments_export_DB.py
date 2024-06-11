import sqlite3
import datetime

# Define the SQLite database file
database_file = 'redditComments.sqlite'

# Connect to the SQLite database
conn = sqlite3.connect(database_file)
cursor = conn.cursor()

# Retrieve all records from the redditComments table
cursor.execute('SELECT formatted_timestamp, comment_link, upvote_count, comment_body FROM redditComments ORDER BY formatted_timestamp DESC')
comments = cursor.fetchall()

# Generate filename with date and time
current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime('%Y%m%d_%H%M%S_%A')
file_name = f'reddit_comments_{formatted_datetime}.log'

# Write the comments to the file in the specified format
with open(file_name, 'w', encoding='utf-8') as file:
    for comment in comments:
        formatted_timestamp, comment_link, upvote_count, comment_body = comment

        file.write('************************\n')
        file.write(f'{formatted_timestamp}\n')
        file.write('************************\n')
        file.write(f'{comment_link}\n')
        file.write(f'Upvotes: {upvote_count}\n\n')
        file.write(f'{comment_body}\n\n\n')

# Close the database connection
conn.close()

print(f'Comments exported to -- {file_name}')
