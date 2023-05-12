#!/usr/bin/python3
""" A recursive function that queries the Reddit API """
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ Return the titles of all hot posts for a givn subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'niyi'}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        """valid response"""
        response = response.json().get('data')
        next = response.get('after')
        for post in response.get('children'):
            hot_list.append(post.get('data').get('title'))
        if next:
            return recurse(subreddit, hot_list, after)
        return hot_list
    """invalide response"""
    return (None)
