#!/usr/bin/python

class Post:
    'Class for reddit posts'
    postCount = 0

    # Initialize post object
    def __init__(self, title, id):
        self.title = title
        self.id = id
        self.scoreList = []
        self.minuteList = []
        self.minutes = 0
        Post.postCount += 1

    # Add score to the list
    def addScore(self, score):
        self.scoreList.append(score)
        self.minuteList.append(self.minutes)
        self.minutes = self.minutes + 1

    # Calculate change in scores
    def calculateChange(self):
        slope = []
        sum = 0

        # Calculate slope between each of the consecutive points
        index = len(self.scoreList) - 1
        while index > 0:

            if self.scoreList[index - 1] != 0:
                slope.append(self.scoreList[index] / self.scoreList[index-1])

            index = index - 1

        # Calculate average slope
        for score in self.scoreList:
            sum = sum + score

        return sum/len(self.scoreList)
