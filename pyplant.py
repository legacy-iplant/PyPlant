import requests, time, urllib, getpass

APIHost = 'http://foundation.iplantcollaborative.org'
usr = 'landersda'
psw = ''

creds = ('Iplantuser','Iplantuserpass','010101')

def Validate(user,psw):
	print 'Welcome', user, 'to PyPlant!'
	print 'Your Credentials are saved are saved as a global variable.'
	print 'PyPlant will rememember your information until you exit. \n'
	token = GetToken(user,psw)
	global creds
	creds = (user,psw,token)

def GetToken(user=creds[0], psw=creds[1]):
	req = requests.post(APIHost + '/auth-v1/', auth=(user,psw))
	token = req.json()['result']['token']
	print 'Token is', token
	return token

def RenewToken(user=creds[0], psw=creds[1], token=creds[2]):
	payload = {'token' : token}
	req = requests.post(APIHost + '/auth-v1/renew', auth=(user,psw), data=payload)
	if req.json()['status'] == 'success':
		print 'Token renewed.'

def ListTokens(return_list=False, user=creds[0], psw=creds[1]):
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

def DeleteToken(user=creds[0], token=creds[2]):
	req = requests.delete(APIHost + '/auth-v1/', auth=(user,token))
	if req.json()['status'] == 'success':
		print token, 'deleted.'

def ValidateToken(user=creds[0], token=creds[2]):
	req = requests.get(APIHost + '/auth-v1/', auth=(user,token))
	if req.json()['status'] == 'success':
		print 'Token', token, 'validated.'
	else:
		print 'Token', token, 'does not exist.'

def ListDir(de_path='', user=creds[0], token=creds[2]):
	req = requests.get(APIHost + '/io-v1/io/list/' + user + '/' + de_path, auth=(user,token))
	for item in req.json()['result']:
		print item['name']

def UploadFile(user=creds[0], token=creds[2]):
	payload = 'fileToUpload=test.txt'
	req = requests.post(APIHost + '/io-v1/io/' + user, auth=(user,token), files=payload)
	print req.json()