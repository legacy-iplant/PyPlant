#curl -X GET -sku "landersda:Shadow@3876" https://foundation.iplantc.org/io-v1/io/vaughn/tutorials/wocky.txt

import argparse, getpass, urllib, urllib2, base64, simplejson as json

userid = 'landersda'
token = '24b947fbf00186ac532f136a867ecd07'

req = urllib2.Request('https://foundation.iplantc.org/io-v1/io/vaughn/tutorials/wocky.txt')
base64string = base64.encodestring('%s:%s' % (userid, token)).replace('\n', '')
req.add_header("Authorization", "Basic %s" % base64string)

reader = urllib2.urlopen(req)
print reader.read()