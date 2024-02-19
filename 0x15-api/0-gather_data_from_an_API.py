#!/usr/bin/python3
"""
This script fetches data from a given API URL and displays employee's TODO list progress.
"""

import sys
import requests

def fetch_todo_progress(employee_id):
    """
    Fetches TODO list progress for a given employee ID from the API and prints it.
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        user_name = user_data.get('name')
        user_todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        todo_response = requests.get(user_todo_url)
        
        if todo_response.status_code == 200:
            todo_data = todo_response.json()
            total_tasks = len(todo_data)
            completed_tasks = sum(1 for task in todo_data if task.get('completed'))
            
            print(f"Employee {user_name} is done with tasks({completed_tasks}/{total_tasks}):")
            for task in todo_data:
                if task.get('completed'):
                    print(f"\t{task.get('title')}")
        else:
            print("Failed to fetch TODO data")
    else:
        print("Failed to fetch user data")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        print("Employee ID must be an integer")
        sys.exit(1)

    fetch_todo_progress(int(employee_id))
