import praw
import datetime

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


# Generate filename with date and time
current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime('%Y%m%d_%H%M%S_%A')
file_name = f'reddit_comments_{formatted_datetime}.log'


# Get all comments from the user
comments = reddit.redditor(USERNAME).comments.new(limit=None)


with open(file_name, 'w', encoding='utf-8') as file:
    for comment in comments:
        timestamp = comment.created_utc
        dt = datetime.datetime.fromtimestamp(timestamp)
        formatted_timestamp = dt.strftime('%Y-%m-%d %H:%M:%S')
        upvote_count = comment.score
        comment_link = f'https://www.reddit.com{comment.permalink}'

        file.write('************************\n')
        file.write(f'{formatted_timestamp}\n')
        file.write('************************\n')
        file.write(f'{comment_link}\n')
        file.write(f'Upvotes: {upvote_count}\n\n')
        file.write(f'{comment.body}\n\n\n')

print('Saved to -- ', file_name)
