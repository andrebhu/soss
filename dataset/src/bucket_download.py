#!/usr/bin/env python3

import time
import requests
from requests.adapters import HTTPAdapter, Retry

s = requests.Session()

retries = Retry(total=5, 
                backoff_factor=0.1,
                status_forcelist=[500, 502, 503, 504])

s.mount('http://', HTTPAdapter(max_retries=retries))


url = "https://storage.googleapis.com/andrebhu-personal/stackoverflow_answers/"

num_buckets = 116
start = 0

def main():
    for i in range(start, num_buckets):
        bucket_url = url + str(i).zfill(12)
        r = s.get(bucket_url)
        open(f'{str(i).zfill(12)}.gz', 'wb').write(r.content)
        print(time.ctime(), "Downloaded bucket", str(i))

if __name__ == "__main__":
    main()