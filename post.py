#!/usr/bin/python

import json


class RedditPost:

    # Initialize post object
    def __init__(self, title, post_id):
        self.title = title
        self.post_id = post_id
        self.score_list = []
        self.time_list = []

    # Add score to the list
    def add_score(self, score):
        self.score_list.append(score)

    # Add time to list
    def add_time(self, time):
        self.time_list.append(time)

    # Calculate change in scores
    def get_json(self):

        json_obj = {
            'id': self.post_id,
            'title': self.title,
            'score_list': self.score_list,
            'time_list': self.time_list
        }

        return json.dumps(json_obj, indent=2)
