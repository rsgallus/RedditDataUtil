#!/usr/bin/python
import praw
import time

user_agent = ("Analytics Bot 0.1")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("askreddit")

tracked_posts = []

print "\n\n"
for submission in subreddit.get_new(limit = 10):
    tracked_posts.append(submission.id)

    print "---------------------------------"
    print "Tracking Post: ", submission.title
    print "Score: ", submission.score
    print "---------------------------------\n"

count = 1

while count < 6:
    print "\nwaiting 60 seconds\n"
    print "count = ", count
    count = count + 1

    time.sleep(60)
