##Copyright 2015 Christopher King
##This file is part of Pennslyvania Weather Closings.
##
##Pennslyvania Weather Closings is free software: you can redistribute it and/or modify
##it under the terms of the GNU General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##Pennslyvania Weather Closings is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU General Public License for more details.
##
##You should have received a copy of the GNU General Public License

from bs4 import BeautifulSoup as soup
from urllib import urlopen
import re
from itertools import chain

javascript = re.compile(r"ibsys.htvClosings.init\(({.*?})\)") #The closings are embeded in a javascript function. This will extract the dictionary to group 1.
wgalAddress = "http://www.wgal.com/weather/closings"
def closingDictionary(useCache=True, cache="closings.html"):
    """Returns a dictionary containing information about closed schools and bussinesses.

    Keyword Arguments:

    useCache -- If true function will use cache instead of going online (default True)
    cache    -- The file that a cache of the website will be stored in. If none or the file does not exist, useCache will be changed to True (default \"closing.html\")
    """
    if not cache: useCache = False
    if useCache:
        try:
            with open(cache, 'r') as cacheFile:
                wgalSite = cacheFile.read()
        except IOError:
            return closingDictionary(updateCache=False, cache=cache)
    else:
        wgalSite = urlopen(wgalAddress).read()
        if cache:
            with open(cache, 'w') as cacheFile:
                cacheFile.write(wgalSite)

    wgal = soup(wgalSite, 'lxml')
    script = wgal.find(text = javascript)
    rawData = eval(re.search(javascript, script).group(1)) #The parsed data is a valid python dictionary
    organizedDict = {place.pop('name'): place for place in #Change the name into the key
                     chain(*(letter['institutions'] for letter in rawData.values() if type(letter) == dict))} #The raw data is organized by letter. Extract "institutions" from each and chain them together.
    return organizedDict
