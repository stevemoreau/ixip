#!/usr/bin/env python

import cherrypy

# radioChannels = {
    # "333001": [ "Haard As A Rock Radio Channel", "http://184.107.185.106:8000/listen.pls", 32 ],
 # "71478": [ "Nashville Edge", "http://streaming.radionomy.com/NashvilleEdge", 128 ]
   # "71478": [ "Nashville Edge", "http://31.12.64.203/NashvilleEdge", 128 ]
    # "71478": [ "Nashville Edge", "http://listen.radionomy.com:80/europamusic", 128 ]    
# }

radioChannels = {
    "333001": [ "Hard As A Rock Radio Channel", "http://192.168.0.2:8000/hardasarock.mp3", 128 ],
    "333002": [ "Radio Steve", "http://192.168.0.2:8000/stream.m3u", 128 ],
    "333003": [ "100 XR", "http://107.170.188.129:80/listen.pls", 128 ],
    "333004": [ "181 FM", "http://relay1.181.fm:8064/listen.pls", 128 ],
    "333005": [ "4UHardFM", "http://listen.radionomy.com/4u-hard-fm.pls", 128 ],
    "71478": [ "Nashville Edge", "http://192.168.0.2:8000/nashvilleedge.mp3", 128 ]    
}

main='''<?xml version="1.0" encoding="iso-8859-1" standalone="yes" ?>
<ListOfItems>
<ItemCount>-1</ItemCount>
<Item>
<ItemType>Dir</ItemType>
<Title>My Favourites</Title>
<UrlDir>http://pri.wifiradiofrontier.com/setupapp/fs/asp/browsexml/FavXML.asp?empty=</UrlDir>
<UrlDirBackUp>http://sec.wifiradiofrontier.com/setupapp/fs/asp/browsexml/FavXML.asp?empty=</UrlDirBackUp>
</Item>
<Item>
<ItemType>Dir</ItemType>
<Title>Local France</Title>
<UrlDir>http://pri.wifiradiofrontier.com/setupapp/fs/asp/BrowseXML/navXML.asp?gofile=LocationLevelFour-Europe-France&amp;bkLvl=LocationLevelFour-Europe-FranceOObkLvlTypeOOl</UrlDir>
<UrlDirBackUp>http://sec.wifiradiofrontier.com/setupapp/fs/asp/BrowseXML/navXML.asp?gofile=LocationLevelFour-Europe-France&amp;bkLvl=LocationLevelFour-Europe-FranceOObkLvlTypeOOl</UrlDirBackUp>
</Item>
<Item>
<ItemType>Dir</ItemType>
<Title>Stations</Title>
<UrlDir>http://pri.wifiradiofrontier.com/setupapp/fs/asp/BrowseXML/navXML.asp?gofile=Radio</UrlDir>
<UrlDirBackUp>http://sec.wifiradiofrontier.com/setupapp/fs/asp/BrowseXML/navXML.asp?gofile=Radio</UrlDirBackUp>
</Item>
<Item>
<ItemType>Dir</ItemType>
<Title>Podcasts</Title>
<UrlDir>http://pri'''


class IXipSearch(object):
    exposed = True
    def __call__(self, *things):
        self.things = list(things)
        return('Test IXipSearch {}'.format(self.things))

    def loginXML_asp(self, token=0, gofile=None, mac="4c799d6b5bac0d271dff2cc35921dd31", dlang="eng", fver=1):
        print 'IXipSearch login={}'.format(token)
        if gofile is not None:
            return self.FavXML_asp(sFavName="Steve")
        else:
            return '''<EncryptedToken>3a3f5ac48a1dab4e</EncryptedToken>'''
    loginXML_asp.exposed = True
    
    def Search_asp(self, sSearchtype=3, Search=333001, mac="4c799d6b5bac0d271dff2cc35921dd31", dlang="eng", fver=1):
        print 'IXipSearch search={}'.format(Search)
        channel = radioChannels[Search]
        return '''<?xml version="1.0" encoding="iso-8859-1" standalone="yes" ?>
<ListOfItems>
<ItemCount>1</ItemCount>
<Item>
<ItemType>Previous</ItemType>
<UrlPrevious>http://pri.wifiradiofrontier.com/setupapp/fs/asp/BrowseXML/loginXML.asp?gofile=</UrlPrevious>
<UrlPreviousBackUp>http://sec.wifiradiofrontier.com/setupapp/fs/asp/BrowseXML/loginXML.asp?gofile=</UrlPreviousBackUp>
</Item>
<Item>
<ItemType>Station</ItemType>
<StationId>{}</StationId>
<StationName>{}</StationName>
<StationUrl>{}</StationUrl>
<StationDesc></StationDesc>
<Logo></Logo>
<StationFormat>Rock</StationFormat>
<StationLocation>US</StationLocation>
<StationBandWidth>{}</StationBandWidth>
<StationMime>MP3</StationMime>
<StationProto>http</StationProto>
<Relia>5</Relia>
</Item>
</ListOfItems>'''.format(Search, channel[0], channel[1], channel[2])
    Search_asp.exposed = True
    
    def FavXML_asp(self, empty="", sFavName="Steve", startItems=1, endItems=100, mac="4c799d6b5bac0d271dff2cc35921dd31", dlang="eng", fver=1):
        print 'IXipSearch favorites name={}'.format(sFavName)
        response = '''<?xml version="1.0" encoding="iso-8859-1" standalone="yes" ?>
<ListOfItems>
<ItemCount>1</ItemCount>
<Item>
<ItemType>Previous</ItemType>
<UrlPrevious>http://pri.wifiradiofrontier.com/setupapp/fs/asp/BrowseXML/loginXML.asp?gofile=</UrlPrevious>
<UrlPreviousBackUp>http://sec.wifiradiofrontier.com/setupapp/fs/asp/BrowseXML/loginXML.asp?gofile=</UrlPreviousBackUp>
</Item>
<Item>
<ItemType>Dir</ItemType>
<Title>Steve</Title>
<UrlDir>http://pri.wifiradiofrontier.com/setupapp/fs/asp/browsexml/FavXML.asp?empty=&amp;sFavName=Steve</UrlDir>
<UrlDirBackUp>http://sec.wifiradiofrontier.com/setupapp/fs/asp/browsexml/FavXML.asp?empty=&amp;sFavName=Steve</UrlDirBackUp>
</Item>
</ListOfItems>
'''
        if sFavName is not None:
            response = '''<?xml version="1.0" encoding="iso-8859-1" standalone="yes" ?>
<ListOfItems>
<ItemCount>{}</ItemCount>
<Item>
<ItemType>Previous</ItemType>
<UrlPrevious>http://pri.wifiradiofrontier.com/setupapp/fs/asp/browsexml/FavXML.asp?empty=gofile=</UrlPrevious>
<UrlPreviousBackUp>http://sec.wifiradiofrontier.com/setupapp/fs/asp/browsexml/FavXML.asp?empty=gofile=</UrlPreviousBackUp>
</Item>
'''.format(len(radioChannels))
            for channelID, channel in radioChannels.iteritems():
                response += '''<Item>
<ItemType>Station</ItemType>
<StationId>{}</StationId>
<StationName>{}</StationName>
<Bookmark>http://pri.wifiradiofrontier.com/setupapp/fs/asp/browsexml/RemoveFavs.asp?empty=&amp;ID={}&amp;ShowID=0&amp;sFavName=Steve</Bookmark>
</Item>
'''.format(channelID, channel[0], channelID)
            response += '''</ListOfItems>
'''
        return response
    FavXML_asp.exposed = True


if __name__ == '__main__':
    print "Starting cherrypy server"
    
    cherrypy.config.update({
      'server.socket_host' : '0.0.0.0',
      'server.socket_port' : 8118,
    })
  
    cherrypy.tree.mount(IXipSearch(), '/setupapp/fs/asp/BrowseXML/')
    cherrypy.tree.mount(IXipSearch(), '/setupapp/fs/asp/browsexml/')

    print "Starting cherrypy server"
    #cherrypy.engine.signals.subscribe()
    cherrypy.engine.start()
    cherrypy.engine.block()

