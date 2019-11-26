#!/usr/bin/env python3
import random
from datetime import datetime
import bogoemail

def is_sorted(data):
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True

def bogosort_sort(data):
    while not is_sorted(data):
        random.shuffle(data)
    return data

data = []
for i in range(random.randint(10,15)):
    data.append(random.randint(0,100))
unsorted = data[:]

lucky_numbers = ""
for i in range(5):
    lucky_numbers += f"{random.randint(0,100)}  "

write_path = '/path/to/output.log'

picnic_error_catcher = 1

def main():
    log = open(write_path, 'w')
    log.write(f"[{datetime.now()}] unsorted:    {unsorted}\n")        
    log.close()

    startdate = datetime.today()
    start = datetime.now()
    bogosort_sort(data)
    enddate = datetime.today()
    end = datetime.now()

    elapsed = end-start

    log=open(write_path, 'w')
    log.write(f"[{datetime.now()}] sorted:      {data}\n")
    log.close()

    bogoemail.send(data, unsorted, elapsed, startdate, enddate, lucky_numbers)
    

if __name__ == '__main__':
    if(picnic_error_catcher):
        print("please read the code before running it, it can do bad things")
        exit()
    main()
