#!/usr/bin/python3
"""
Export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(url + "/users").json()
    todos = requests.get(url + "/todos").json()

    todo_dict = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        tasks = [{"username": username, "task": task.get("title"), "completed": task.get("completed")} for task in todos if task.get("userId") == user_id]
        todo_dict[str(user_id)] = tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(todo_dict, json_file)
