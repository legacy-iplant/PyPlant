import requests, time, urllib, getpass

APIHost = 'http://foundation.iplantcollaborative.org'
usr = 'landersda'
psw = 'Shadow@3876'

def GetToken(user, psw):
	req = requests.post(APIHost + '/auth-v1/', auth=(user,psw))
	token = req.json()['result']['token']
	print 'Token is', token
	return token

def RenewToken(user, psw, token):
	payload = {'token' : token}
	req = requests.post(APIHost + '/auth-v1/renew', auth=(user,psw), data=payload)
	if req.json()['status'] == 'success':
		print 'Token renewed.'

def ListTokens(user, psw, return_list=False):
	req = requests.get(APIHost + '/auth-v1/list', auth=(user,psw))
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
	if req.json()['status'] == 'success':
		print token, 'deleted.'

def ValidateToken(user, token):
	req = requests.get(APIHost + '/auth-v1/', auth=(user,token))
	if req.json()['status'] == 'success':
		print 'Token', token, 'validated.'
	else:
		print 'Token', token, 'does not exist.'

def ListDir(user, token, de_path=''):
	req = requests.get(APIHost + '/io-v1/io/list/' + user + '/' + de_path, auth=(user,token))
	print req.url
	for item in req.json()['result']:
		print item['name']

def UploadFile(user, token):
	payload = {'fileToUpload' : '@test.txt', 'fileType' : 'FASTA-0'	}
	req = requests.post('https://foundation.iplantc.org/io-v1/io/' + user, auth=(user,token), data=payload)
	print req.url
	print req.json()

def DeleteFile(user, token, de_path=''):
	req = requests.delete(APIHost + '/io-v1/io/' + user + '/' + de_path, auth=(user,token))
	print req.url
	print req.json()

