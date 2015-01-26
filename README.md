# Pennsylvania-Weather-Closings
Have you ever had a project where you needed to know if your school or bussiness is closed or delayed? Your problem is solved!

This program will scrap the page at http://www.wgal.com/weather/closings. (Pennslyvania-Weather-Closings nor its authors are affiliated with WGAL.)

```
>>> from weatherScrapper import closings
>>> closings()
{'Dixon Univ Center-Harrisburg': {'status': 'Saturday: Closed', 'emailListKey': 'lan_closingsibstandard119', 'updateTimestamp': '2015-01-23T15:16:00.000-06:00', 'address': 'Harrisburg / Dauphin / PA'}, 'Dillsburg Area Public Library': {'status': 'Saturday: Closed', 'emailListKey': 'lan_ ...
```

Note that this function will place a cache of the file in `closings.html`. If you do want a cache, do

```
>>> closings(cache=None)
```

or if you want to update the cache you already have

```
closings(useCache=False)
```

It could theortically be used with other programming Languages by simply running it like this:

```
$ python2 weatherScrapper.py
Dixon Univ Center-Harrisburg
	STATUS: Saturday: Closed
	EMAILLISTKEY: lan_closingsibstandard119
	UPDATETIMESTAMP: 2015-01-23T15:16:00.000-06:00
	ADDRESS: Harrisburg / Dauphin / PA
Dillsburg Area Public Library
	STATUS: ...
```

Here is its command line info.

```
usage: weatherScrapper.py [-h] [--usecache] [--verbose] [--cache CACHE]

Process closing information from external website

optional arguments:
  -h, --help     show this help message and exit
  --usecache     use the HTML cached on the local machine
  --verbose      write debugging to stderr
  --cache CACHE  name of the cache file
```

Want to help? See [the wiki](../../wiki).

![GPL 3 Licensed](https://www.gnu.org/graphics/gplv3-127x51.png)

## Noncoders
This program is designed to be included in other programs. For example, I made this so I could make a raspberry pi alarm  clock that would allow me to sleep in if there was no school. If have an idea for how this could be used, sumbit it as an Issue.
