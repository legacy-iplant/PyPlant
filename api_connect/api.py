#!/usr/bin/env python
import argparse
import getpass
import urllib
import urllib2
import base64
 
parser = argparse.ArgumentParser(description='Authentication test using foundation api.')
parser.add_argument('--U', dest='userid', type=str,
                   help='Your iPlant Username')
parser.add_argument('--P',dest='password', type=str,
					help='Your iPlant password')
 
args = parser.parse_args()
userid = args.userid
password = args.password
url = "https://foundation.iplantc.org/auth-v1/"
req = urllib2.Request(url)
base64string = base64.encodestring('%s:%s' % (userid, password)).replace('\n', '')
req.add_header("Authorization", "Basic %s" % base64string)
print(req.get_method())
result = urllib2.urlopen(req)
print(result.read())