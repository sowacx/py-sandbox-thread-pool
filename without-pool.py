import asyncio
import concurrent.futures
import logging
import sys
from time import sleep
import requests
import functools
import datetime


def print_qwe(task_number, second_param):
    response = requests.get("http://google.com", headers=second_param)
    return task_number


def run_print_qwe_in_pool(total_tasks):
    HEADER1 = {"Dummy": 'dummy-value'}
    for i in range(total_tasks):
        print_qwe(i, HEADER1)


def main():    
    total_tasks = 400  # Set the total number of tasks
    step_one = datetime.datetime.utcnow()
    print (f'before call for add_checksum_doclink timestamp: {str(datetime.datetime.utcnow())}')
    # Run the main function within the event loop
    run_print_qwe_in_pool(total_tasks)
    step_two = datetime.datetime.utcnow()
    print(f'after call for add_checksum_doclink timestamp: {str(datetime.datetime.utcnow())}')
    # Calculate the time difference
    time_difference = step_two - step_one
    # Extract seconds and microseconds
    seconds = time_difference.total_seconds()
    milliseconds = int((time_difference.microseconds + time_difference.seconds * 10**6) / 1000)
    print(f"Time difference in seconds: {seconds} seconds")
    print(f"Time difference in milliseconds: {milliseconds} milliseconds")


# Call the main function
main()
