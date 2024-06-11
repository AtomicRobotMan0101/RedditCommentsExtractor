import praw
import datetime
import sqlite3

# Reddit API credentials
CLIENT_ID = 'FILLMEINN'
CLIENT_SECRET = 'FILLMEINN'
USERNAME = 'FILLMEINN'
PASSWORD = 'FILLMEINN'
USER_AGENT = 'TCCscript'

# Initialize the Reddit API
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    username=USERNAME,
    password=PASSWORD,
    user_agent=USER_AGENT
)

# Connect to SQLite database
conn = sqlite3.connect('redditComments.sqlite')
cursor = conn.cursor()

# Create table schema if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS redditComments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    formatted_timestamp TEXT,
    comment_link TEXT UNIQUE,
    upvote_count INTEGER,
    comment_body TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS redditCommentsHistory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    comment_id INTEGER,
    formatted_timestamp TEXT,
    comment_link TEXT,
    upvote_count INTEGER,
    comment_body TEXT,
    FOREIGN KEY(comment_id) REFERENCES redditComments(id)
)
''')

# Get all comments from the user
comments = reddit.redditor(USERNAME).comments.new(limit=None)

for comment in comments:
    timestamp = comment.created_utc
    dt = datetime.datetime.fromtimestamp(timestamp)
    formatted_timestamp = dt.strftime('%Y-%m-%d %H:%M:%S')
    upvote_count = comment.score
    comment_link = f'https://www.reddit.com{comment.permalink}'
    comment_body = comment.body

    # Check if comment exists
    cursor.execute("SELECT id, comment_body FROM redditComments WHERE comment_link=?", (comment_link,))
    result = cursor.fetchone()
    
    if result:
        comment_id = result[0]
        existing_body = result[1]

        # Update comment score and body if they have changed
        cursor.execute('''
        UPDATE redditComments 
        SET upvote_count=?, comment_body=? 
        WHERE id=?
        ''', (upvote_count, comment_body, comment_id))

        # If comment body has changed, save to history table
        if existing_body != comment_body:
            cursor.execute('''
            INSERT INTO redditCommentsHistory (comment_id, formatted_timestamp, comment_link, upvote_count, comment_body) 
            VALUES (?, ?, ?, ?, ?)
            ''', (comment_id, formatted_timestamp, comment_link, upvote_count, existing_body))
    else:
        # Insert new comment
        cursor.execute('''
        INSERT INTO redditComments (formatted_timestamp, comment_link, upvote_count, comment_body) 
        VALUES (?, ?, ?, ?)
        ''', (formatted_timestamp, comment_link, upvote_count, comment_body))

# Commit and close database connection
conn.commit()
conn.close()

print('Comments saved to SQLite database.')
