import schedule as sc
import time

def task1():
    print("Task 1 executed")

def task2():
    print("Task 2 executed")

def task3():
    print("Task 3 executed")

# Schedule task1 to run every 1 hour
sc.every(1).hours.do(task1)

# Schedule task2 to run every 9am
sc.every().day.at("09:00").do(task2)

# Schedule task3 to run every monday at 9am
sc.every().monday.at("09:00").do(task3)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    sc.run_pending()
    time.sleep(1)
