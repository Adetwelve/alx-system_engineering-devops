#!/usr/bin/python3
"""A script using REST API for Query"""
import json
import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com"
    user_ep = "{}/users/".format(url)
    todo_ep = "{}/todos/".format(url)
    user_name = requests.get(user_ep).json()
    todo = requests.get(todo_ep).json()
    todo_usr = {u.get('id'): [{"username": u.get('username'),
                               "task":  t.get('title'),
                               "completed": t.get('completed')}
                              for t in todo if t.get('userId') == u.get('id')]
                for u in user_name
                }
    # save in a json file
    with open('todo_all_employees.json', 'w', encoding='utf-8') as f:
        json.dump(todo_usr, f)
