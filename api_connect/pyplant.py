import requests

def GetToken(user, psw):
	res = requests.post('http://foundation.iplantc.org/auth-v1/', auth=(user,psw))
	tok = res.json()['result']['token']
	print tok
	return tok

