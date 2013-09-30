## Put token here
token = '24b947fbf00186ac532f136a867ecd07'

import argparse, getpass, urllib, urllib2, base64, simplejson as json

"""
This is Python code for connecting to the Foundation API.
"""

def main():

	global userid, password, task, result, just_result

	parser = argparse.ArgumentParser(description='Authentication test using foundation api.')
	parser.add_argument('-u', dest='userid', type=str,
	                   help='Your iPlant Username')
	parser.add_argument('-o', dest='options', type=str,
						help='Extra options')
	parser.add_argument(dest='task', type=str,
						help='The task you wish to complete')
	 
	args = parser.parse_args()
	userid = args.userid
	task = args.task
	options = args.options

	if task.lower() == 'list_analyses':
		get('https://foundation.iplantc.org/io-v1/io/list/' + userid + '/analyses')
	if task.lower() == 'list_tokens':
		get('https://foundation.iplantc.org/auth-v1/list')
	if task.lower() == 'show_home':
		get('https://foundation.iplantc.org/io-v1/io/list/' + userid)

def get(url):
	req = urllib2.Request(url)
	print "This will be a", req.get_method(), "request."

	base64string = base64.encodestring('%s:%s' % (userid, token)).replace('\n', '')
	req.add_header("Authorization", "Basic %s" % base64string)

	opener = urllib2.build_opener()
	results = opener.open(req)
	data = json.load(results)
	result = data.get('result')
	for item in result:
		print(json.dumps(item, sort_keys=True, indent=4 * ' '))

if __name__ == '__main__':
	main()