#!/usr/bin/python
import praw
import datetime
import calendar
import csv

def main():

    # Config
    column_headers = True
    post_limit = 200

    # Initialize our bot
    reddit = praw.Reddit(
        client_id='QiTk8CZr-w7kwQ',
        client_secret='DyRNXYDdquexl-n3l9cb1Df709Y',
        user_agent='RedditDataUtil-1.0')

    # Select a subreddit
    subreddit = reddit.subreddit("askreddit")

    # Initialize array for posts
    data_list = []

    # Append column headers
    if column_headers:
        headers = []
        headers.append("id")
        headers.append("title")
        headers.append("username")
        headers.append("serious")
        headers.append("time_of_day")
        headers.append("day_of_week")
        headers.append("upvote_count")
        headers.append("comment_count")
        headers.append("comment_upvote_sum")
        headers.append("elapsed_time")
        headers.append("title_word_count")
        data_list.append(headers)

    # Collect posts
    print "Grabbing new posts"
    row_count = 0
    for submission in subreddit.rising(limit=post_limit):

        # Create new row
        row = []

        # Check our progress
        row_count += 1
        if row_count % 10 == 0:
            print row_count, 'posts read'

        # Find basic post information
        row.append(submission.id)
        row.append(submission.title.encode('utf-8').strip())
        row.append(submission.author.name.encode('utf-8').strip())

        # Find serious tag
        if '[serious]' in submission.title.lower():
            row.append(1)
        else:
            row.append(0)

        # Find time of day
        current_hour = datetime.datetime.now().hour
        if current_hour < 4:                            # midnight - 4am
            row.append("night")
        elif current_hour >= 4 and current_hour < 8:     # 4am - 8am
            row.append("early_morning")
        elif current_hour >= 8 and current_hour < 12:    # 8am - noon
            row.append("morning")
        elif current_hour >= 12 and current_hour < 16:    # noon - 4pm
            row.append("afternoon")
        elif current_hour >= 16 and current_hour < 20:    # 4pm - 8pm
            row.append("early_evening")
        elif current_hour >= 20 and current_hour < 24:    # 8pm - midnight
            row.append("evening")

        # Find day of week
        row.append(calendar.day_name[datetime.datetime.now().weekday()].lower())

        # Find upvote count
        row.append(submission.score)

        # Find comment count
        row.append(submission.num_comments)

        # Find top-level comment score sum
        submission.comments.replace_more(limit=0)
        score_sum = 0
        for comment in submission.comments:
            score_sum += comment.score
        row.append(score_sum)

        # Find elapsed time
        posted_time = datetime.datetime.fromtimestamp(submission.created_utc)
        elapsed_time = (datetime.datetime.now() - posted_time).total_seconds() / 60.0
        row.append(int(round(elapsed_time)))

        # Find title word count
        row.append(submission.title.count(' ') + 1)

        # Add row to data list
        data_list.append(row)

    # Write to csv file
    with open("output.csv", "wb") as outputfile:
        print 'Writing to csv'
        csvwriter = csv.writer(outputfile)
        csvwriter.writerows(data_list)


if __name__ == '__main__':
    main()
