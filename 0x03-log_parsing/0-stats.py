#!/usr/bin/env python3
"""Log parsing script"""


import sys


total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for i, line in enumerate(sys.stdin):
        if i % 10 == 0 and i > 0:
            print(f"Total file size: {total_size}")
            for status_code in sorted(status_counts.keys()):
                if status_counts[status_code] > 0:
                    print(f"{status_code}: {status_counts[status_code]}")
        try:
            fields = line.split()
            file_size = int(fields[-1])
            status_code = int(fields[-2])
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
        except (ValueError, IndexError):
            pass
except KeyboardInterrupt:
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")
