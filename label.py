#!/usr/bin/python
import praw
import csv

def main():

    # Initialize our bot
    reddit = praw.Reddit(
        client_id='QiTk8CZr-w7kwQ',
        client_secret='DyRNXYDdquexl-n3l9cb1Df709Y',
        user_agent='RedditDataUtil-1.0')

    # Initialize array for posts
    data_list = []

    # Open csv file
    with open("output.csv", "rb") as inputfile:

        # Initialize a csv reader
        print "Labeling posts"
        csvreader = csv.reader(inputfile, delimiter=',')
        row_count = 0

        # Read csv
        for row in csvreader:

            # Append column header
            if row_count == 0:
                row.append("label")

            # Append label
            else:
                submission = reddit.submission(id=row[0])

                if int(submission.score) > 5000:
                    row.append(1)
                else:
                    row.append(0)

            # Append row
            data_list.append(row)

            # Check our progress
            row_count += 1
            if row_count % 10 == 0:
                print row_count, 'posts labeled'

    # Write to csv file
    with open("labeled_output.csv", "wb") as outputfile:
        print 'Writing to csv'
        csvwriter = csv.writer(outputfile)
        csvwriter.writerows(data_list)


if __name__ == '__main__':
    main()
