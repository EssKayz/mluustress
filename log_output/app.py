#!/usr/bin/env python3

import time
import random
import string
from datetime import datetime

# Generate random string on startup
RANDOM_STRING = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

if __name__ == "__main__":
    while True:
        timestamp = datetime.now().isoformat()
        print(f"{timestamp} - {RANDOM_STRING}", flush=True)
        time.sleep(5)
