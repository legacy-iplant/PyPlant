import requests, time

def GetToken(user, psw):
	req = requests.post('http://foundation.iplantc.org/auth-v1/', auth=(user,psw))
	tok = req.json()['result']['token']
	print 'Token is', tok
	return tok

def RenewToken(user, psw, token):
	payload = {'token' : token}
	req = requests.post('http://foundation.iplantc.org/auth-v1/renew', auth=(user,psw), data=payload)
	if req.json()['status'] == 'success':
		print 'Token renewed.'

def ListTokens(user, psw, return_list=False):
	req = requests.get('http://foundation.iplantc.org/auth-v1/list', auth=(user,psw))
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
	req = requests.delete('http://foundation.iplantc.org/auth-v1/', auth=(user,token))
	if req.json()['status'] == 'success':
		print token, 'deleted.'

def ValidateToken(user, token):
	req = requests.get('http://foundation.iplantc.org/auth-v1/', auth=(user,token))
	if req.json()['status'] == 'success':
		print 'Token', token, 'validated.'
	else:
		print 'Token', token, 'does not exist.'