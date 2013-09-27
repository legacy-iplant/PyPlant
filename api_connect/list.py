#!/usr/bin/env python
import argparse
import getpass
import urllib
import urllib2
import base64
 
parser = argparse.ArgumentParser(description='Authentication test using foundation api.')
parser.add_argument('--U', dest='userid', type=str,
                   help='Your iPlant Username')
parser.add_argument('--P', dest='password', type=str,
					help='Your iPlant password')
parser.add_argument('--T',dest='token', type=str,
					help='Your valid iPlant token')
 
args = parser.parse_args()
userid = args.userid
token = args.token
password = args.password
url = "https://foundation.iplantc.org/io-v1/io/list/landersda/analyses"
req = urllib2.Request(url)
print "This will be a", req.get_method(), "request."

base64string = base64.encodestring('%s:%s' % (userid, token)).replace('\n', '')
req.add_header("Authorization", "Basic %s" % base64string)

opener = urllib2.build_opener()
results = opener.open(req)
for item in results:
	print item