# Pennsylvania-Weather-Closings
Have you ever had a project where you needed to know if your school or bussiness is closed or delayed? Your problem is solved!

This program will scrap the page at http://www.wgal.com/weather/closings. (Pennslyvania-Weather-Closings nor its authors are affiliated with WGAL.)

To get started, first run the following to command:
```
pip2 install beautifulsoup4 lxml
```
as root. Then it is as simple as this:
```
>>> import weatherScrapper
>>> weatherScrapper.closingDictionary()
{'Dixon Univ Center-Harrisburg': {'status': 'Saturday: Closed', 'emailListKey': 'lan_closingsibstandard119', 'updateTimestamp': '2015-01-23T15:16:00.000-06:00', 'address': 'Harrisburg / Dauphin / PA'}, 'Dillsbur
...
3:00.000-06:00', 'address': 'Jacobus / York / PA'}, 'HACC - Gettysburg Campus': {'status': 'Saturday: Closed', 'emailListKey': 'lan_closingsibstandard11', 'updateTimestamp': '2015-01-23T22:49:00.000-06:00', 'address': 'Gettysburg / Adams / PA'}}
```

Note that this function will place a cache of the file in `closings.html`. If you do want a cache, do.
```
>>> weatherScrapper.closingDictionary(cache=None)
```

or if you want to update the cache you already have

```
weatherScrapper.closingDictionary(useCache=False)
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

Not that callling it like this always sets `usecache` to false. (Want to help? Add commandline arguments to this.)

## Noncoders
This program is designed to be included in other programs. For example, I made this so I could make a raspberry pi alarm  clock that would allow me to sleep in if there was no school. If have an idea for how this could be used, sumbit it as an Issue.

![GPL 3 Licensed](https://www.gnu.org/graphics/gplv3-127x51.png)
