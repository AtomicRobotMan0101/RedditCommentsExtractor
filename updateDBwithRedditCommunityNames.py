import sqlite3
import re


def add_column_to_table(db_name, table_name, column_name, column_type):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Adding a new column to the table
    cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type};")

    conn.commit()
    conn.close()


def extract_community_name(url):
    match = re.search(r'reddit\.com/r/([^/]+)/', url)
    if match:
        return match.group(1)
    return None


def update_reddit_community(db_name, table_name, url_column, community_column):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Fetch all rows
    cursor.execute(f"SELECT rowid, {url_column} FROM {table_name}")
    rows = cursor.fetchall()

    # Update each row with the extracted community name
    for rowid, url in rows:
        community_name = extract_community_name(url)
        if community_name:
            cursor.execute(f"UPDATE {table_name} SET {community_column} = ? WHERE rowid = ?", (community_name, rowid))

    conn.commit()
    conn.close()


# Adding the new column
# add_column_to_table('database.db', 'redditComments', 'reddit_community', 'TEXT')

# Updating the new column with the extracted community names
update_reddit_community('redditComments.sqlite', 'redditComments', 'comment_link', 'reddit_community')
