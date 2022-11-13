#!/usr/bin/env python3

import time
import requests

url = "https://storage.googleapis.com/andrebhu-personal/stackoverflow_answers/"

num_buckets = 116
start = 18

def main():
    for i in range(start, num_buckets):
        bucket_url = url + str(i).zfill(12)
        r = requests.get(bucket_url)
        open(f'{str(i).zfill(12)}.gz', 'wb').write(r.content)
        print(time.ctime(), "Downloaded bucket", str(i))

if __name__ == "__main__":
    main()