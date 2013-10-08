import requests, time, urllib, getpass

APIHost = 'https://foundation.iplantcollaborative.org'

""" 
Change the username and password to reflect your own if you
don't want to have to type it out every time.
"""

usr = 'dalanders'
psw = 'Shadow@3876'

"""
If retJSON is True, then all functions will return only JSON objects.
This is done to allow developers to use the machine-reading functions,
instead of the human-reading functions.

Put simply, mark retJSON as True if you want the functions to be 
machine readable, and false if you want them to be human readbale.
"""

retJSON = False

def WriteFile(obj, file):
	with open(file, 'r+') as myopenfile:
		myopenfile.write(obj)

def GetToken(user, psw):
	global retJSON
	req = requests.post(APIHost + '/auth-v1/', auth=(user, psw))
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	token = req.json()['result']['token']
	print 'Token is', token
	return token

def RenewToken(user, psw, token):
	global retJSON
	payload = {'token' : token}
	req = requests.post(APIHost + '/auth-v1/renew', auth=(user, psw), data=payload)
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	if req.json()['status'] == 'success':
		print 'Token renewed.'

def ListTokens(user, psw, return_list=False):
	global retJSON
	req = requests.get(APIHost + '/auth-v1/list', auth=(user, psw))
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	if len(req.json()['result']) > 0:
		print 'Token Credentials for', req.json()['result'][0]['username'], '\n'
		for row in req.json()['result']:
			print row['token'], 'expires on', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(row['expires']))
		if return_list == True and len(req.json()['result']) > 1:
			token_list = []
			for row in req.json()['result']:
				token_list.append(row['token'])
			return token_list
		elif return_list == True and len(req.json()['result']) == 1:
			return req.json()['result'][0]['token']
	else:
		print 'No active credentials.'

def DeleteToken(user, token):
	global retJSON
	req = requests.delete(APIHost + '/auth-v1/', auth=(user, token))
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	if req.json()['status'] == 'success':
		print token, 'deleted.'
	else:
		print 'Error'

def ValidateToken(user, token):
	global retJSON
	req = requests.get(APIHost + '/auth-v1/', auth=(user, token))
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	if req.json()['status'] == 'success':
		print 'Token', token, 'validated.'
	else:
		print 'Token', token, 'does not exist.'

def ListDir(user, token, path=''):
	global retJSON
	req = requests.get(APIHost + '/io-v1/io/list/' + user + '/' + path, auth=(user, token))
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	print 'Directory \n'
	for item in req.json()['result']:
		print item['name'], '[', item['type'], ']'

def UploadFile(user, token, file):
	global retJSON
	with open(file, 'rb') as myfile:
		gear = myfile.read()
	payload = {'fileToUpload' : (file, gear)}
	req = requests.post(APIHost + '/io-v1/io/' + user, auth=(user, token), files=payload)
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	print 'File Information \n'
	for item in req.json()['result']:
		print item, ':', req.json()['result'][item]

""" 
Had so much trouble with uploading files that I'm holding on to this UploadFile2 function which was
the original one that worked.
"""

def UploadFile2(user, token):
	global retJSON
	payload = {'fileToUpload' : 'Hello, World!', 'fileType' : 'FASTA-0'	}
	req = requests.post('https://foundation.iplantcollaborative.org/io-v1/io/' + user, auth=(user, token), files=payload)
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	print req.json()

def Delete(user, token, path='test.txt'):
	global retJSON
	req = requests.delete(APIHost + '/io-v1/io/' + user + '/' + path, auth=(user, token))
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	if req.json()['status'] == 'success':
		print path, 'deleted.'

def DownloadFile(user, token, path='test.txt'):
	global retJSON
	req = requests.get(APIHost + '/io-v1/io/' + user + '/' + path, auth=(user, token))
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	return req.text

def Rename(user, token, path='test.txt', new_name='new_name.txt'):
	global retJSON
	payload = {'action' : 'rename', 'newName' : new_name}
	req = requests.put(APIHost + '/io-v1/io/' + user + '/' + path, auth=(user, token), data=payload)
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	if req.json()['status'] == 'success':
		print path, 'changed to', new_name 

def MakeDir(user, token, new_folder='new_folder', path=''):
	global retJSON
	payload = {'action' : 'mkdir', 'dirName' : new_folder}
	req = requests.put(APIHost + '/io-v1/io/' + user + '/' + path, auth=(user, token), data=payload)
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	if req.json()['status'] == 'success':
		print path + '/' + new_folder, 'created.'

"""
MoveFile currently doesn't work.
"""

def MoveFile(user, token, path, new_path):
	global retJSON
	payload = {'action' : 'move', 'newPath' : '/' + user + '/' + new_path}
	req = requests.put(APIHost + '/io-v1/io/' + user + '/' + path, auth=(user, token), data=payload)
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	print req.json()
	if req.json()['status'] == 'success':
		print path, 'moved to', new_path

def ListApps(user, token, print_connect=True):
	global retJSON
	req = requests.get(APIHost + '/apps-v1/apps/list', auth=(user, token))
	if print_connect == True:
		print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	for item in req.json()['result']:
		print item['id']

def ListSharedApps(user, token):
	global retJSON
	req = requests.get(APIHost + '/apps-v1/apps/share/list', auth=(user, token))
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	for item in req.json()['result']:
		print item['id']

def PLINK(user, token, jobname, inputPED, inputMAP, archivepath, softwarename='plink-1.07u1', requestedtime='24:00:00',
			arguments='--assoc --adjust --allow-no-sex --out simulation1_--assoc'):
	global retJSON
	payload = {'jobName' : jobname, 'softwareName' : softwarename, 'archivePath' : archivepath, 
		'requestedTime' : requestedtime, 'inputPED' : inputPED, 'inputMAP' : inputMAP, 
		'arguments' : arguments, 'archive' : 'True'}
	req = requests.post(APIHost + '/apps-v1/job', auth=(user, token), data=payload)
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	if req.json()['status'] == 'success':
		print 'Job', req.json()['result']['id'], 'submitted.'
	else:
		print req.json()['message']

def CheckJobStatus(user, token, jobid):
	global retJSON
	req = requests.get(APIHost + '/apps-v1/job/' + str(jobid), auth=(user, psw))
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	print str(jobid), 'STATUS:', req.json()['result']['status']