#!/usr/bin/python3
"""A script using REST API for Query"""
import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com"
    e_id = int(sys.argv[1])
    user_ep = "{}/users/{}".format(url, e_id)
    todo_ep = "{}/todos/".format(url)
    emp_name = requests.get(user_ep).json().get('name')
    todo = requests.get(todo_ep).json()
    tod_arg = [tod for tod in todo if tod.get('userId') == e_id]
    num_t = len(tod_arg)
    tod_ct = [to for to in tod_arg if to.get('completed')]
    num_ct = len(tod_ct)

    print("Employee {} is done with tasks({}/{}):"
          .format(emp_name, num_ct, num_t))

    for task in tod_ct:
        print("\t {}".format(task.get("title")))
