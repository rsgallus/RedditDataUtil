#!/usr/bin/python
import praw
import time
import datetime
import post


def main():

    # Constants
    update_interval = 10    # Minutes
    post_limit = 20         # Posts

    reddit = praw.Reddit(
        client_id='my client id',
        client_secret='my client secret',
        user_agent='my user agent')

    # Initialize our bot
    user_agent = "Analytics Bot 0.1"
    r = praw.Reddit(user_agent=user_agent)

    # Select a subreddit
    subreddit = r.get_subreddit("askreddit")

    # Initialize array for tracked posts
    tracked_posts = []

    # Begin main execution loop
    while True:

        # Grab any new posts
        print("\n ---------------------------------- \n Checking for new posts \n")
        for submission in subreddit.get_new(limit=post_limit):

            # Create a new post object
            new_post = post.Post(submission.title, submission.id)

            if new_post not in tracked_posts:
                tracked_posts.append(new_post)
                print("New Post: ", new_post.title)

        # Track score changes
        minutes = update_interval
        while minutes > 0:
            print("\n\n Updating tracked posts")

            for current_post in tracked_posts:
                submission = r.get_submission(submission_id=current_post.id)
                current_post.add_score(submission.score)
                current_time = time.time();
                current_post.add_time(datetime.datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S'))

            print("\n Minutes remaining = ", minutes)
            minutes -= 1

            time.sleep(60)  # Wait 60 seconds


if __name__ == '__main__':
    main()
