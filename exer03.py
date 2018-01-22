#!/usr/bin/env python3

import re

logfile = 'mini-access-log.txt'

sample = '67.218.116.165 - - [30/Jan/2010:00:03:18 +0200] "GET /robots.txt HTTP/1.0" 200 99 "-" "Mozilla/5.0 (Twiceler-0.9 http://www.cuil.com/twiceler/robot.html)"'
test_ip = '67.218.116.165'
test_ts = '30/Jan/2010:00:03:18 +0200'
test_req = 'GET /robots.txt HTTP/1.0'


def parse_entry(line):
    ip = line[:line.find(' ')]
    ts = line[line.find('[')+1:line.find(']')]

    start = line.find('"') + 1
    end = line.find('"', start)
    req = line[start:end]
    return ip, ts, req


def parse_entry_re(line):
    search_pattern = r'(\d+.\d+.\d+.\d+).*\[(.*)\] "(.*?)"'
    mo = re.search(search_pattern, line)

    ip = mo.group(1)
    ts = mo.group(2)
    req = mo.group(3)
    return ip, ts, req


if __name__ == '__main__':
    assert parse_entry(sample) == (test_ip, test_ts, test_req)
    assert parse_entry_re(sample) == (test_ip, test_ts, test_req)

    logs = []
    with open(logfile, 'r') as f:
        while True:
            single_entry = f.readline().strip()
            if not single_entry:
                break
            ip_address, timestamp, request = parse_entry_re(single_entry)
            entry = {'ip_address': ip_address, 'timestamp': timestamp, 'request': request}
            logs.append(entry)

    print(logs)
