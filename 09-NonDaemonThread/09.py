from threading import Thread
import time

def show_timer():
    count = 0
    while True:
        count += 1
        time.sleep(1)
        print(f"Has been waiting for {count} second(s) ...")

# Non daemon thread
t = Thread(target=show_timer)
t.start()

answer = input("Do you want to exit? \n")