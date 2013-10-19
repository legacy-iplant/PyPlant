## PyPlant
## Python classes and functions for interacting with iPlant Collaborative's Foundation API

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

## Examples of common tasks
```python
usr = 'dalanders'
psw = PSW()
```
Authenticate a token:
```python
token = GetToken(usr,psw)
```
See all my tokens and their expirations:
```python
ListTokens(usr,token)
```
Return a list of all my tokens:
```python
token_list = ListTokens(usr,token,True)
```
Delete a token:
```python
DeleteToken(usr,token)
```
Renew a token for another 2 hours:
```python
RenewToken(usr,psw,token)
```
Validate a token (make sure it still works):
```python
ValidateToken(usr,token)
```
See folders and files in your home directory:
```python
ListDir(usr,token)
```
See folders an files in your analyses directory:
```python
ListDir(usr,token,'analyses')
```
Delete all my tokens:
```python
token_list = ListTokens(usr,token,return_list=True)
for item in range(len(token_list)):
	DeleteToken(usr,token_list[item])
```	
Upload a file to your main home directory on iPlant:
```python
UploadFile(usr,token,'fileImuploading.txt')
```
Download a file from your analyses folder:
```python
myfile = DownloadFile(usr,token,'analyses/myanalysis.csv')
```
Write the file to your working directory:
```python
WriteFile(myfile,'placeinmyhomedirectory.csv')
```
Delete a file in my iPlant directory:
```python
Delete(usr,token,'fileImuploading.txt')
```
Rename a file in my iPlant directory:
```python
Rename(usr,token,'fileImuploading.txt','thenewname.txt')
```
Make a new directory:
```python
MakeDir(usr,token,'new_folder')
```
List all available apps on the Foundational API:
```python
ListApps(usr,token)
```
List all apps shared with you:
```python
ListSharedApps(usr,token)
```
Launch a PLINK job:
```python
PLINK(usr,token,jobname='myjob','\dalanders\simulation1.ped','\dalanders\simulation1.map',archivepath='\dalanders\analyses')
```
Check on a job's status:
```python
CheckJobStatus(usr,token,24948)
```
Using the data class:
```python
myfile = DownloadFile(usr,token,'\analyses\myanalysis\filetodownload.txt')
mydata = Data(myfile)

## Return headers
mydata.headers

## Return number of rows
mydata.nrow

## Return number of columns
mydata.ncol

## Return row 3
mydata.data[3]

## Return 'SNP' column vector
mydata.data['SNP']

## Write a CSV file
mydata.WriteCSV('/users/dustin/desktop/mydata.txt')
```
## License

GNU GPL-v3
