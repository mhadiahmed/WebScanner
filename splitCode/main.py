#!/usr/bin/python3
#script created by  " Mhadi Ahmed"
#web scanner 
#Work on linux and need some tools like whois , nmap
#Copyright  2016 the 'Sudan H4x0r' Team.  
import os
from urllib import request
import io
from tld import get_tld

def create_dir(directory):
	if not os.path.exists(directory):
	   os.makedirs(directory)
	
def write_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()

def get_whois(url):
	command = 'whois ' + url
	process = os.popen(command)
	results = str(process.read())
	return results

def get_IP(url):
	command = 'host ' + url
	process = os.popen(command)
	results = str(process.read())
	marker  = results.find('has address')+12
	return results
	

def get_domain(url):
	domain_name = get_tld(url)
	return domain_name
	
def get_nmap(options, ip):
	command = 'nmap ' + options + ' ' + ip
	process = os.popen(command)
	results = str(process.read())
	return results

def get_rbotes(url):
	if url.endswith('/'):
	    path = url
	else:
		path = url + '/'
	req = request.urlopen(path + 'robots.txt', data=None)
	data = io.TextIOWrapper(req , encoding = 'utf-8')
	return data.read()

ROOT_DIR = 'RsultScanner'
create_dir(ROOT_DIR)

def Scanner(name , url):
	domain_name = get_domain(url)
	ip_Address = get_IP(url)
	nmap = get_nmap('-F' , domain_name)
	robots_txt = get_rbotes(url)
	whois = get_whois(domain_name)
	create_report(name, url , domain_name, nmap, robots_txt, whois)

def create_report(name, url , domain_name, nmap, robots_txt, whois):
	ScannRuslt = ROOT_DIR + '/' + name
	create_dir(ScannRuslt)
	write_file(ScannRuslt + '/full_url.txt', url)
	write_file(ScannRuslt + '/domain_name.txt', domain_name)
	write_file(ScannRuslt + '/nmap.txt', nmap)
	write_file(ScannRuslt + '/robots_txt.txt', robots_txt)
	write_file(ScannRuslt + '/whois.txt', whois)

#import your site url with https:// or http:// to git your result 
Scanner('name of the file', 'https://www.example.com')
