## PyPlant
## Python functions for interacting with iPlant Collaborative's Foundation API

## Project
Description: Python functions for interfacing with iPlant Collaborative's Foundation API.
It provides a framework to begin developing Python scripts for interacting with the API 
layer. At this point, there are no plans to develop a full scale environment, but instead
provide a set of functions and classes that can be deployed in any user-designed script or program.In other words, the goal is to provide some tools to build your own tools, instead of a full-scale environment for interacting with iPlant. 

## Project Setup
If you wish to contribute to the master function and class set, please contact me.

Using Python 2.7.5, there is only one dependency which must be installed. It is the
requests library (docs.python-requests.org/‎). To install it, unzip the tarball, browse
to the folder containing those files, and type: "python setup.py install" in your
terminal command-line.

### Examples of common tasks
'''
usr = 'dalanders'
psw = PSW()
'''
### Authenticate a token:
'''
token = GetToken(usr,psw)
'''
See all my tokens and their expirations:
ListTokens(usr,token)

Return a list of all my tokens:
token_list = ListTokens(usr,token,True)

Delete a token:
DeleteToken(usr,token)

Renew a token for another 2 hours:
RenewToken(usr,psw,token)

Validate a token (make sure it still works):
ValidateToken(usr,token)

See folders and files in your home directory:
ListDir(usr,token)

See folders an files in your analyses directory:
ListDir(usr,token,'analyses')

Delete all my tokens:
for item in range(len(token_list)):
	DeleteToken(usr,token[item])
	
Upload a file to your main home directory on iPlant:
UploadFile(usr,token,'fileImuploading.txt')

Download a file from your analyses folder:
myfile = DownloadFile(usr,token,'analyses/myanalysis.csv')

Write the file to your working directory:
WriteFile(myfile,'placeinmyhomedirectory.csv')

Delete a file in my iPlant directory:
Delete(usr,token,'fileImuploading.txt')

Rename a file in my iPlant directory:
Rename(usr,token,'fileImuploading.txt','thenewname.txt')

Make a new directory:
MakeDir(usr,token,'new_folder')

List all available apps on the Foundational API:
ListApps(usr,token)

List all apps shared with you:
ListSharedApps(usr,token)

Launch a PLINK job:
PLINK(usr,token,jobname,archivepath='analyses','simulation1.ped','simulation1.map')

Check on a job's status:
CheckJobStatus(usr,token,24948)

## License

GNU GPL-v3