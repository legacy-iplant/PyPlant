## Put token here
token = 'f9fc5647d53a4766f6094440ff571ced'

import argparse, getpass, urllib, urllib2, base64, simplejson as json

"""
This is Python code for connecting to the Foundation API.
"""

def main():

	global userid, password, task, data

	parser = argparse.ArgumentParser(description='Authentication test using foundation api.')
	parser.add_argument('-u', dest='userid', type=str,
	                   help='Your iPlant Username')
	parser.add_argument('-d', dest='data', type=str,
						help='Post data')
	parser.add_argument(dest='task', type=str,
						help='The task you wish to complete')
	 
	args = parser.parse_args()
	userid = 'landersda'
	task = args.task
	data = args.data

	if task.lower() == 'list_analyses':
		get_json('https://foundation.iplantc.org/io-v1/io/list/' + userid + '/analyses')
	if task.lower() == 'list_tokens':
		get_json('https://foundation.iplantc.org/auth-v1/list')
	if task.lower() == 'show_home':
		get_json('https://foundation.iplantc.org/io-v1/io/list/' + userid)
	if task.lower() == 'upload':
		post('https://foundation.iplantc.org/io-v1/io/' + userid, data)
	if task.lower() == 'get_jobs':
		get_json('https://foundation.iplantc.org/apps-v1/jobs/list')
	if task.lower() == 'test_wocky':
		get('https://foundation.iplantc.org/io-v1/io/vaughn/tutorials/wocky.txt')
	if task.lower() == 'list_apps':
		get_apps()

def get_json(url):
	req = urllib2.Request(url)
	print "This is a", req.get_method(), "request."

	base64string = base64.encodestring('%s:%s' % (userid, token)).replace('\n', '')
	req.add_header("Authorization", "Basic %s" % base64string)

	opener = urllib2.build_opener()
	results = opener.open(req)
	data = json.load(results)
	result = data.get('result')
	for item in result:
		print(json.dumps(item, sort_keys=True, indent=4 * ' '))

def get(url):
	req = urllib2.Request(url)
	print "This is a", req.get_method(), "request."

	base64string = base64.encodestring('%s:%s' % (userid, token)).replace('\n', '')
	req.add_header("Authorization", "Basic %s" % base64string)

	reader = urllib2.urlopen(req)
	print reader.read()

def get_apps():
	req = urllib2.Request('https://foundation.iplantc.org/apps-v1/apps/list')
	print "This is a", req.get_method(), "request."

	base64string = base64.encodestring('%s:%s' % (userid, token)).replace('\n', '')
	req.add_header("Authorization", "Basic %s" % base64string)

	opener = urllib2.build_opener()
	results = opener.open(req)
	data = json.load(results)
	result = data.get('result')
	for item in result:
		print(json.dumps(item['id'], sort_keys=True, indent=4 * ' '))

def post(url, data):
	post_data = urllib.urlencode(data)
	print post_data
	req = urllib2.Request(url, post_data)
	print "This is a", req.get_method(), "request."

	base64string = base64.encodestring('%s:%s' % (userid, token)).replace('\n', '')
	req.add_header("Authorization", "Basic %s" % base64string)

	reader = urllib2.urlopen(req)
	print reader.read()

if __name__ == '__main__':
	main()