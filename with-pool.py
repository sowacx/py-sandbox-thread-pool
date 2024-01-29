import asyncio
import concurrent.futures
import logging, sys
import requests
import functools
import datetime
import aiohttp

async def print_qwe(task_number, second_param):
    async with aiohttp.ClientSession() as session:
        async with session.get("http://google.com", headers=second_param) as response:
            # You can await response.text() or any other asynchronous operation here
            x =response.status

    return task_number

 

async def run_print_qwe_in_pool(pool_size, total_tasks):
    semaphore = asyncio.Semaphore(pool_size)

    async def worker(task_number):
        async with semaphore:
            HEADER1 = {"Dummy": 'dummy-value'}
            partial_func = functools.partial(print_qwe, task_number, second_param=HEADER1)
            veeva_request = await loop.run_in_executor(None, partial_func)
            veeva_request_response = await veeva_request
    tasks = [worker(i) for i in range(total_tasks)]
    await asyncio.gather(*tasks)

 

def main():
    pool_size = 10  # Set the thread pool size limit
    total_tasks = 400  # Set the total number of tasks

    step_one = datetime.datetime.utcnow()
    print(f'before call for add_checksum_doclink timestamp: {str(datetime.datetime.utcnow())}')

    # Run the main function within the event loop
    loop.run_until_complete(run_print_qwe_in_pool(pool_size, total_tasks))

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
loop = asyncio.get_event_loop()
main()