# coding:utf-8
import urllib
import urllib2
url='http://www.vzhusu.com/forum.php'
postdata={'username':'sikozheng','password':'siko6161'}
data=urllib.urlencode(postdata)
req=urllib2.Request(url,data)
response=urllib2.urlopen(req)
html=response.read()
print(html)

