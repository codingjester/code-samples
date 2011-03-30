#!/usr/bin/env python
import os
from datetime import datetime, timedelta

"""
You have a 1 million line tab-delimited text file with the following data:
timestamp   web_site    remote_ip

Example:
2010-01-01 12:34:56     http://somewhere.com/document.html      123.123.123.123

Data has been collecting in the file for the past 3 months.

Write a program to calculate the IP address that generated the most hits yesterday based on the data located in this file.
"""


def reverse_readline(file):
    """
    A reverse reader that uses python's generator ability
    so that we can easily iterate and yield once we find
    a new line. 
    
    Argument:
        file - a file object
    Yields:
        A buffer of a line once it sees too many newlines
    Limitations:
        I'm not sure if this will work on a windows box.
        Seek apparently can perform strangely on windows.
    """
    #Go to the end of the file
    file.seek(0,2)
    size = file.tell()
    buffer = ''
    for position in xrange(1, size+2):
        char = file.read(1)
        if char == '\n' and '\n' in buffer:
            yield buffer
            buffer = ''
        buffer = char + buffer
        if position > size:
            yield buffer
            return
        file.seek(-1*position, 2)

def find_highest_hit_ip(file):
    """
    Finds the highest hit count of the ip addresses that is
    in the file object you pass it. We read the file reversed,
    because we assume that it's a log file, which means most current
    entries are appended to the end. We ignore the current date logs,
    add in yesterdays logs and if we see 2 days ago, we break the loop
    because we've gone too far. This saves memory and allows us to read
    extremely large files.
    
    Arguments:
        file - a string, the path to the file or the file name if it's in the current
               directory
    Returns:
        a tuple of the ip address that has the highest hit and it's count.

    Notes:
        This could easily be modified to sort and pull in the top 10 ips
        or something.
    """
    file = open(file, 'r')
    #Get the date for 1 day ago
    yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    #Get the date for 2 days ago
    two_days = (datetime.today() - timedelta(days=2)).strftime('%Y-%m-%d')
    ips = {}
    for line in reverse_readline(file):
        #if we start seeing two days ago, just stop.
        if two_days in line:
            break
        if yesterday in line:
            ip = line.rstrip().split('\t')[-1]
            if ip in ips:
                ips[ip] += 1
            else:
                ips[ip] = 1
    file.close()
    #As of 2.5+ you can find the max of a dict by this snippet
    max_ip = max(ips, key=lambda a: ips.get(a))
    return max_ip, ips[max_ip]

#Example Usage
print find_highest_hit_ip('iplist.log')

#Example of bad usage :D
#print find_highest_hit_ip('1')
