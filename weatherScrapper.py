from bs4 import BeatifulSoup as soup
from urllib import urlopen
import re
from itertools import chain

javascript = re.compile(r"ibsys.htvClosings.init\(({.*?})\)")
wgalAddress = "http://www.wgal.com/weather/closings"
def closingDictionary():
    wgal = soup(urlopen(wgalAddress), 'lxml')
    script = wgal.find(text = javascript)
    rawData = eval(re.search(javascript, script).group(1))
    organizedDict = {place.pop('name'): place for place in chain(*(letter['institution'] for letter in rawData.values() if type(letter) == dict))}
    return organizedDict
