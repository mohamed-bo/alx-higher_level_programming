#!/usr/bin/python3
import sys


status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}


def pri_info():
    print('File size: {:d}'.format(file_size))

    for key, value in sorted(status_codes.items()):
        if value > 0:
            print('{}: {:d}'.format(key, value))


count = 0
file_size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            pri_info()

        linee = line.split()
        try:
            status = int(linee[-2])
            if str(status) in status_codes.keys():
                status_codes[str(status)] += 1
        except [KeyError, IndexError]:
            pass
        try:
            file_size += int(linee[-1])
        except [KeyError, IndexError]:
            pass
        count += 1
    pri_info()
except KeyboardInterrupt:
    pri_info()
    raise
