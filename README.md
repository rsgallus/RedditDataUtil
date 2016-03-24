# RedditBot
A simple reddit bot that follows the new section of AskReddit and predicts which posts will be successful.

Note that this is a work in progress.


## Description
This project uses the Python Reddit API Wrapper (PRAW) and some other simple Python libraries to retrieve new posts from the AskReddit section of Reddit. It then tracks changes in the score of each post over time. After sufficient data has been gathered, it predicts how successful the post will be based on the slop of the data points.

## Future Development
As of now, the slope of the data points over time is the only metric being used to estimate the success of each post. For future development, the plan is to use Tensor Flow, an open source computational library, to train a simple machine learning model. The model will then make predictions based on previously gathered data.
