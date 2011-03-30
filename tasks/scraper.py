#!/usr/bin/env python
from lxml.html import fromstring
import urllib2

"""
Write a program that takes a URL to an HTML document as an argument, fetches the document, 
extracts and prints all URLs contained within, and then repeats the process recursively for 
each URL it found, up to a configurable depth.
"""


def grabLinks(url, depth, path=[]):
    """
    This is really a DFS problem with a limitation on depth. I wrote
    a standard recursive DFS algo but added a return of the path once we go too deep.
    
    Arguments:
        url - a string of the base url, preferably without the trailing/
        depth - an int, the depth you want to go before stopping
        path - a list of strings, the path we've currently gone down. This way
               we won't go over the same page over and over again.
    Returns:
        path - a list of all the links we have traversed. There should be
               no dupes.
    Limitations:
        The web is always moving, so depending on the site, we might break on
        certain things in the href.
    """
    path += [url]
    if depth == 0: return path
    page = fromstring(urllib2.urlopen(url).read())
    #Convenience to make all links absolute. Easier to deal with.
    page.make_links_absolute(url)
    links = [link.get('href') for link in page.cssselect('a[href]')]
    for link in links:
        #Make sure we don't get things we don't like.
        #This should be improved a bit...kinda hackish and fragile?
        if link not in ('#') and 'mailto:' not in link and 'javascript:' not in link:
            if link not in path:
                try:
                    path = grabLinks(link, depth-1, path)
                except urllib2.HTTPError, e:
                    #If we get a 404, we just return the current link rather than try to keep going.
                    #It's a dead path, but still a node.
                    path += [link]
    return path

#Usage for link grabbing.
#I'm printing the list only because it's trivial to print all links.
print grabLinks('http://www.google.com', 2)

