import requests, time, urllib, getpass

APIHost = 'https://foundation.iplantcollaborative.org'
usr = 'dalanders'
psw = 'Shadow@3876'

def GetToken(user, psw):
	req = requests.post(APIHost + '/auth-v1/', auth=(user,psw))
	print 'Connected to', req.url
	token = req.json()['result']['token']
	print 'Token is', token
	return token

def RenewToken(user, psw, token):
	payload = {'token' : token}
	req = requests.post(APIHost + '/auth-v1/renew', auth=(user,psw), data=payload)
	print 'Connected to', req.url
	if req.json()['status'] == 'success':
		print 'Token renewed.'

def ListTokens(user, psw, return_list=False):
	req = requests.get(APIHost + '/auth-v1/list', auth=(user,psw))
	print 'Connected to', req.url
	if len(req.json()['result']) > 0:
		print 'Token Credentials for', req.json()['result'][0]['username'], '\n'
		for row in req.json()['result']:
			print row['token'], 'expires on', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(row['expires']))
		if return_list == True:
			token_list = []
			for row in req.json()['result']:
				token_list.append(row['token'])
			return token_list
	else:
		print 'No active credentials.'

def DeleteToken(user, token):
	req = requests.delete(APIHost + '/auth-v1/', auth=(user,token))
	print 'Connected to', req.url
	if req.json()['status'] == 'success':
		print token, 'deleted.'

def ValidateToken(user, token):
	req = requests.get(APIHost + '/auth-v1/', auth=(user,token))
	print 'Connected to', req.url
	if req.json()['status'] == 'success':
		print 'Token', token, 'validated.'
	else:
		print 'Token', token, 'does not exist.'

def ListDir(user, token, de_path=''):
	req = requests.get(APIHost + '/io-v1/io/list/' + user + '/' + de_path, auth=(user,token))
	print 'Connected to', req.url
	print 'Directory \n'
	for item in req.json()['result']:
		print item['name'], '[', item['type'], ']'

def UploadFile(user, token, file, filetype='FASTA-0'):
	with open(file, 'rb') as myfile:
		gear = myfile.read()
	payload = {'fileToUpload' : ('test.txt', gear), 'fileType' : 'FASTA-0'}
	req = requests.post(APIHost + '/io-v1/io/' + user, auth=(user,token), files=payload)
	print 'Connected to', req.url
	for item in req.json()['result']:
		print item, ':', req.json()['result'][item]

""" 
Had so much trouble with uploading files that I'm holding on to this UploadFile2 function which was
the original one that worked.
"""

def UploadFile2(user, token):
	payload = {'fileToUpload' : 'Hello, World!', 'fileType' : 'FASTA-0'	}
	req = requests.post('https://foundation.iplantcollaborative.org/io-v1/io/' + user, auth=(user,token), files=payload)
	print 'Connected to', req.url
	print req.json()

def DeleteFile(user, token, de_path='test.txt'):
	req = requests.delete(APIHost + '/io-v1/io/' + user + '/' + de_path, auth=(user,token))
	print 'Connected to', req.url
	if req.json()['result'] == 'success':
		print de_path, 'deleted.'

def DownloadFile(user, token, de_path='test.txt', save=False, save_file='try_write.txt'):
	req = requests.get(APIHost + '/io-v1/io/' + user + '/' + de_path, auth=(user, token))
	print 'Connected to', req.url
	if save == True:
		with open(save_file, 'r+') as sf:
			sf.write(req.text)
	else:
		return req.text

def RenameFile(user, token, de_path='test.txt', new_name='new_name.txt'):
	payload = {'action' : 'rename', 'newName' : new_name}
	req = requests.put(APIHost + '/io-v1/io/' + user + '/' + de_path, auth=(user, token), data=payload)
	print 'Connected to', req.url
	if req.json()['status'] == 'success':
		print de_path, 'changed to', new_name 


