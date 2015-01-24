##Copyright 2015 Christopher King
##This file is part of Foobar.
##
##Foobar is free software: you can redistribute it and/or modify
##it under the terms of the GNU General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##Foobar is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU General Public License for more details.
##
##You should have received a copy of the GNU General Public License

from bs4 import BeautifulSoup as soup
from urllib import urlopen
import re
from itertools import chain

javascript = re.compile(r"ibsys.htvClosings.init\(({.*?})\)")
wgalAddress = "http://www.wgal.com/weather/closings"
def closingDictionary(updateCache=False, cache="closings.html"):
    '''Returns a dictionary containing information about closed schools and bussinesses.'''
    if not cache: updateCache = True
    if updateCache:
        wgalSite = urlopen(wgalAddress).read()
        if cache:
            with open(cache, 'w') as cacheFile:
                cacheFile.write(wgalSite)
    else:
        try:
            with open(cache, 'r') as cacheFile:
                wgalSite = cacheFile.read()
        except IOError:
            return closingDictionary(updateCache=True, cache=cache)

    wgal = soup(wgalSite, 'lxml')
    script = wgal.find(text = javascript)
    rawData = eval(re.search(javascript, script).group(1))
    organizedDict = {place.pop('name'): place for place in chain(*(letter['institutions'] for letter in rawData.values() if type(letter) == dict))}
    return organizedDict
