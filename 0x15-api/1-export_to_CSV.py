#!/usr/bin/python3

"""A script using REST API for Query"""

import csv
import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com"
    user_id = int(sys.argv[1])
    user_ep = "{}/users/{}".format(url, user_id)
    todo_ep = "{}/todos/".format(url)
    user_name = requests.get(user_ep).json().get('username')
    todo = requests.get(todo_ep).json()
    todo_usr = [[user_id, user_name, t.get('completed'), t.get('title')]
                for t in todo if user_id == t.get('userId')]

    # open a file for writing a csv format

    with open('{}.csv'.format(user_id), 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(todo_usr)
