import time
from datetime import datetime, timedelta

class Clock:

    def __init__(self):
        '''Intialize the start time and end for 1 hour timer'''
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(hours=1)

    def hour_timer(self):
        print(f"Timer started: {self.start_time.strftime('%H:%M:%S')}")

        #Loop until 1 hour has passed
        while datetime.now() < self.end_time:
            now = datetime.now()
            print(now.strftime('%H:%M:%S'))
            time.sleep(1)

def main():
    instance = Clock()
    instance.hour_timer()

main()