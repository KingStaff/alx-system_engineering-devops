#!/usr/bin/python3
"""Module for task 2"""

import requests

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-User-Agent"}
    params = {"limit": 100, "after": after}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return None
    
    data = response.json()
    
    if 'data' in data and 'children' in data['data']:
        children = data['data']['children']
        hot_list.extend([child['data']['title'] for child in children])

    after = data['data']['after'] if 'data' in data and 'after' in data['data'] else None

    if after is None:
        if not hot_list:
            return None
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
