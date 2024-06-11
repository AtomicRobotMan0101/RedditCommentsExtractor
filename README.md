
### Purpose

Save all of your Reddit comments to a text file or database.

### Difficulty

- Easy Peasy to use
- A tiny bit of config to register you with Reddits API (below)
- Minor usage requirements (below)

### The Problem

- Reddit does not offer a simple tool to dump ones comments
- This is useful if your posts, comments or account is summarily blasted by the various Admin Overlords... :(

### WHAT

There are 3 main scripts:

    * one to rip down comments and stuff them into a SQLlite database
    * one to rip down comments and burp them into a text file, with a dated name
    * one to query the database and burp out text files in the same format as the file script

A fourth script will _update the databases existing records_ with the Community Name.  This is of little use to most. Its purpose was for statistical analysis. 

### USAGE

From the terminal command line type: `python3 reddit_comments_scrape_DB.py`

The script will:

    * rip down the last 1000 comments
    * create a database schema if it does not already exist
    * stuff the comments into the DB

Fields saved are the:

    * Time of your comment
    * Comment link (URL)
    * Up/down vote count
    * Full text in markdown

If the script is run periodically it will also:

    * Update the latest vote count
    * Copy the latest comment text, if changed (i.e. you edited it)
    * Place "old" comments into another table for historical reference

This way, as your comments gain in popularity over time (or not!) the tally/vote will be kept.

Also, should your text be edited, the changes can be seen over time. (I occasionally edit my tech answers for **surious tpyos**)

### SCRIPT REQUIREMENTS

You will need to install the PIPs `praw` and `sqlite3`.  Also `re` and `datetime` if you are missing them.

- `pip3 install praw, sqlite, re, datetime`

For Debian based Linux you'll also need SQLite and a decent SQL GUI browser:

- `sudo apt install sqlite3 sqlitebrowser` 

For other Linux and Windows, do what is needed :)

### REGISTRATION

Read this: https://praw.readthedocs.io/en/stable/getting_started/authentication.html

**OR** If you like to **avoid documentation** ;) go here https://old.reddit.com/prefs/apps/ and here https://old.reddit.com/wiki/api#wiki_read_the_full_api_terms_and_sign_up_for_usage

- Ensure you are logged into Reddit
- Register as a developer
- Create credentials

Once that is done, go [here](https://old.reddit.com/prefs/apps/) 
- Go to the click the "**Create Another Ap**" button
- Select **Script**
- Follow your nose

You will have a few strings to fill out in the header of each script. These strings identify you to Reddit.

Here is an **_EXAMPLE_**

    client_id="SI8pN3DSbt0zor"
    client_secret="xaxkj7HNh8kwg8e5t4m6KvSrbTI"
    username="fakebot3"        
    password="1guiwevlfo00esyy"
    user_agent="testscript by u/fakebot3"

### GENERAL COMMENTARY

* The 1000 comment limitation is imposed by Reddit
* Run the script periodically via cron, or manually

I created this as I was _sick to death_ of answering the same questions over and over. I haunt the Linux, tech and n00bie sections and help people. This gives me great joy... however, n00bs DON'T read documentation and always assume their trivial problems are somehow unique.

Rather than using Reddit useless search (and increasingly more useless over time) I was driven to dump all my comments into big text files.  I did this once a week via a cron.

The text files were fine, but searching them was a PITA. Now, with SQLlite, one simply opens the database file and the search is easy.

### ASSISTANCE

If you feel the scripts are missing something, please feel free to make a PR, comment or add a feature request.

I sincerely hope you enjoy using this small tool :)



