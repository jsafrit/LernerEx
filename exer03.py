#!/usr/bin/env python3

sample = '67.218.116.165 - - [30/Jan/2010:00:03:18 +0200] "GET /robots.txt HTTP/1.0" 200 99 "-" "Mozilla/5.0 (Twiceler-0.9 http://www.cuil.com/twiceler/robot.html)"'
ip = '67.218.116.165'
ts = '30/Jan/2010:00:03:18 +0200'
req = 'GET /robots.txt HTTP/1.0'


def parse_entry(line):
    ip = line[:line.find(' ')]
    ts = line[line.find('[')+1:line.find(']')]

    start = line.find('"') + 1
    end = line.find('"', start)
    req = line[start:end]
    return ip, ts, req


if __name__ == '__main__':
    assert(parse_entry(sample) == (ip, ts, req))
