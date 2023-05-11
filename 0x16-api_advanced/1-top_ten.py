#!/usr/bin/python3
"""function that queries the Reddit API and
    prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'niyi'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        """valid response"""
        response = response.json()
        posts = response.get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
    """invalide response"""
    print(None)
