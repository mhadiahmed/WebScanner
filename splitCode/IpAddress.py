import os


def get_IP(url):
	command = 'host ' + url
	process = os.popen(command)
	results = str(process.read())
	marker  = results.find('has address')+12
	return results
print(get_IP('www.google.com'))
	
