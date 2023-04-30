#!/usr/bin/python3

"""A script using REST API for Query"""

import json
import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com"
    user_id = int(sys.argv[1])
    user_ep = "{}/users/{}".format(url, user_id)
    todo_ep = "{}/todos/".format(url)
    user_name = requests.get(user_ep).json().get('username')
    todo = requests.get(todo_ep).json()
    todo_usr = {"user_id": [{"task": t.get('title'),
                             "completed":  t.get('completed'),
                             "username": user_name}
                            for t in todo if t.get('userId') == user_id]
                }
    # save in a json file
    with open("{}.json".format(user_id), 'w', encoding='utf-8') as f:
        json.dump(todo_usr, f)
