import requests, time, csv

APIHost = 'https://foundation.iplantcollaborative.org'

"""
If retJSON is True, then all functions will return only JSON objects.
This is done to allow developers to use the machine-reading functions,
instead of the human-reading functions.

Put simply, mark retJSON as True if you want the functions to be 
machine readable, and false if you want them to be human readbale.
"""

retJSON = False

## This function writes an object as a file exactly how it is
def WriteFile(obj, file):
	with open(file, 'r+') as myopenfile:
		myopenfile.write(obj)

## This function retrieves a token
def GetToken(user, psw):
	global retJSON
	req = requests.post(APIHost + '/auth-v1/', auth=(user, psw))
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	token = req.json()['result']['token']
	print 'Token is', token
	return token

## This function renews a token for 2 more hours, it also
## requires a psw and the token
def RenewToken(user, psw, token):
	global retJSON
	payload = {'token' : token}
	req = requests.post(APIHost + '/auth-v1/renew', auth=(user, psw), data=payload)
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	if req.json()['status'] == 'success':
		print 'Token renewed.'
	else:
		print req.json()['message']

## This function produces all active credentials. If return_list ==
## True, then a list of all tokens is returned
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

## Deletes a given token
def DeleteToken(user, token):
	global retJSON
	req = requests.delete(APIHost + '/auth-v1/', auth=(user, token))
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	if req.json()['status'] == 'success':
		print token, 'deleted.'
	else:
		print req.json()['message']

## Prints whether or not a token currently exists
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

## Lists a directory in the Discovery Environment, [ dir ] if directory,
## [ file ] if its a file. Path extends beyond '/username/'
def ListDir(user, token, path=''):
	global retJSON
	req = requests.get(APIHost + '/io-v1/io/list/' + user + '/' + path, auth=(user, token))
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	print 'Directory \n'
	for item in req.json()['result']:
		print item['name'], '[', item['type'], ']'

## Uploads a file to the main directory only right now
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

## Deletes a file or folder-- Be careful, you can accidently delete your
## entire user if you leave path blank!! It would delete '/username'
def Delete(user, token, path='test.txt'):
	global retJSON
	req = requests.delete(APIHost + '/io-v1/io/' + user + '/' + path, auth=(user, token))
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	if req.json()['status'] == 'success':
		print path, 'deleted.'
	else:
		print req.json()['message']

## Downloads the file to your Python environment. If you want to write a file to your disk,
## use the WriteFile function or transfer it to a Data class and write as a CSV like this:
##
## myfile = DownloadFile(usr,psw,'myfile_on_DE.txt')
## mydata = Data(myfile)
## mydata.WriteCSV('file_in_working_directory.txt') 
def DownloadFile(user, token, path='test.txt'):
	global retJSON
	req = requests.get(APIHost + '/io-v1/io/' + user + '/' + path, auth=(user, token))
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	return req.text

## Rename files or folders in your DE directories
def Rename(user, token, path='test.txt', new_name='new_name.txt'):
	global retJSON
	payload = {'action' : 'rename', 'newName' : new_name}
	req = requests.put(APIHost + '/io-v1/io/' + user + '/' + path, auth=(user, token), data=payload)
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	if req.json()['status'] == 'success':
		print path, 'changed to', new_name 
	else:
		print req.json()['message']

## Make new directories in your DE directories
def MakeDir(user, token, new_folder='new_folder', path=''):
	global retJSON
	payload = {'action' : 'mkdir', 'dirName' : new_folder}
	req = requests.put(APIHost + '/io-v1/io/' + user + '/' + path, auth=(user, token), data=payload)
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	if req.json()['status'] == 'success':
		print path + '/' + new_folder, 'created.'
	else:
		print req.json()['message']

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
	else:
		print req.json()['message']

## List all available apps on the API, plus their corresponding list number
def ListApps(user, token, print_connect=True):
	global retJSON
	item_num = 0
	req = requests.get(APIHost + '/apps-v1/apps/list', auth=(user, token))
	if print_connect == True:
		print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	for item in req.json()['result']:
		print item_num, item['id']
		item_num += 1

## View all apps shared with you
def ListSharedApps(user, token):
	global retJSON
	req = requests.get(APIHost + '/apps-v1/apps/share/list', auth=(user, token))
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	for item in req.json()['result']:
		print item['id']

## Run a PLINK job
def PLINK(user, token, jobname, inputPED, inputMAP, archivepath, arguments='--assoc --adjust --allow-no-sex --out thisjob',
			softwarename='plink-1.07u1', requestedtime='24:00:00'):
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
		return req.json()['result']['id']
	else:
		print req.json()['message']

## Run a FaSTLMM job
def FaSTLMM(usr, token, jobname, inputPED, inputMAP, archivepath, arguments='--assoc --adjust -out thisjob', 
			softwarename='FaST-LMM-1.09u1', requestedtime='24:00:00'):
	global retJSON
	payload = {'jobName' : jobname, 'softwareName' : softwarename, 'archivePath' : archivepath, 
		'requestedTime' : requestedtime, 'inputPED' : inputPED, 'inputMAP' : inputMAP, 'archive' : 'True',
		'arguments' : arguments}
	req = requests.post(APIHost + '/apps-v1/job', auth=(usr, token), data=payload)
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	if req.json()['status'] == 'success':
		print 'Job', req.json()['result']['id'], 'submitted.'
		return req.json()['result']['id']
	else:
		print req.json()['message']

## Check the status of a job, string or integers works
def CheckJobStatus(user, token, jobid):
	global retJSON
	req = requests.get(APIHost + '/apps-v1/job/' + str(jobid), auth=(user, psw))
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	result = req.json()['result']['status']
	print str(jobid), 'STATUS:', result
	if result == 'FAILED':
		print 'MESSAGE:', req.json()['result']['message']

## Shorter named function of the above
def Status(user, token, jobid):
	global retJSON
	req = requests.get(APIHost + '/apps-v1/job/' + str(jobid), auth=(user, psw))
	print 'Connected to', req.url
	if retJSON == True:
		return req.json()
	result = req.json()['result']['status']
	print str(jobid), 'STATUS:', result
	if result == 'FAILED':
		print 'MESSAGE:', req.json()['result']['message']

## Using the corresponding list number, view the required and not-required
## inputs for any given app
def ListAppInputs(user, token, appnum):
	global retJSON
	req = requests.get(APIHost + '/apps-v1/apps/list', auth=(user, token))
	print 'Connected to', req.url
	inputs = req.json()['result'][appnum]['inputs']
	if retJSON == True:
		return inputs
	print req.json()['result'][appnum]['id']
	print '-----------------------------'
	print 'Input Type --- Input Required'
	print '-----------------------------'
	for item in inputs:
		print item['id'], '---', item['value']['required']

"""
Use this Data class to turn downloaded files from the API and 
convert them in to a useable dictionary.

This Data object takes the string returned from the iPlant API,
where all the features of the data are only seperated by only some
spaces. It provides a dictionary object where each key is the row
number and each row number is a list containing that row's data.
"""

class Data:

	def __init__(self, str):
		self.data = self.ChangeToStr(self.Dataize(str), self.nrow)
		self.headers = self.data[0]
		self.ncol = len(self.headers)
		self.MakeColumnVectors()

	## This function takes a string that has been determined by 
	## Dataize to be a row, and returns of list of all the individual
	## words the string (and numbers)
	def Rowize(self, test):
		row = []
		num = 0
		start = 0
		for char in test:
			if char == ' ' and test[num-1] != ' ':
				row.append(test[start:num])
				start = num
			if char != ' ' and test[num-1] == ' ':
				start = num 
			if num == len(test)-1:
				row.append(test[start:num+1])
				start = num
			num += 1
		return row

	## This fucntion searches for what should be a row, sends it
	## to Rowize and then brings it back and logs it in the data
	## dictionary
	def Dataize(self, test):
		data = dict()
		num = 0
		row_num = 0
		for point in range(len(test)+2):
			current_row = test[num:point]
			if current_row.endswith('\n') == True:
				current_row = current_row.strip()
				#print current_row
				data[row_num] = self.Rowize(current_row)
				num = point
				row_num += 1
		self.nrow = row_num - 1
		return data

	## This function changes unicode to regular stringse
	def ChangeToStr(self, data, rows):
		for row in range(rows):
			for cell in range(len(data[row])):
				data[row][cell] = str(data[row][cell])
		return data

	## This function changes numerical rows to floats
	def ChangeToFloat(self, float_col):
		for row in range(1,self.nrow):
			if isinstance(float_col, tuple):
				for cell in float_col:	
					self.data[row][cell] = float(self.data[row][cell])
			else:
				self.data[row][float_col] = float(self.data[row][float_col])

	## This function changes numerical rows to floats
	def ChangeToInt(self, int_col):
		for row in range(1,self.nrow):
			if isinstance(int_col, tuple):
				for cell in int_col:
					self.data[row][cell] = int(self.data[row][cell])
			else:
				self.data[row][int_col] = int(self.data[row][int_col])

	## This function provides extra dictionary references for viewing
	## the column vectors as a list
	## Be careful, after doing this WriteCSV will include additional vectors
	def MakeColumnVectors(self):
		num = 0
		for each in self.headers:
			each_list = list()
			for row in range(1,self.nrow):
				each_list.append(self.data[row][num])
			self.data[each] = each_list
			num += 1

	## Displays the first five rows of the data
	def Head(self):
		if self.nrow > 5:
			for row in range(5):
				print self.data[row]
		else:
			for row in range(self.nrow):
				print self.data[row]

	## This function exports the dictionary to csv
	def WriteCSV(self, file):
		with open(file, 'wb') as csvfile:
			writer = csv.writer(csvfile)
			for row in range(self.nrow):
				if isinstance(row, int):
					writer.writerow(self.data[row])

