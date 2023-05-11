#!/usr/bin/python3
""" function that queries the Reddit API, returns the num subscribers """
import requests


def number_of_subscribers(subreddit):
    """function to check number of users"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Header'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        """Successful response"""
        response = response.json()
        num_sub = response.get('data').get('subscribers')
        return num_sub
    """failed response"""
    return 0
