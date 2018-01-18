# -*- coding: utf-8 -*-
import requests
import json
import random
import sys
import threading
import time

parole = requests.get('https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.txt').text.split('\r\n')
proxy = []

def safe_print(content):
	print("{0}".format(content))

def randomUsername():
	global parole
	return random.choice(parole).lower() + str(random.randint(1000,9000)) + 'ib'

def cookie(proxy):
	return requests.get('https://www.instagram.com/accounts/login', proxies=proxy, headers={'referer':'https://www.instagram.com', 'origin':'https://www.instagram.com/', 'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1'})

def register(data, user, proxy):
	return requests.post('https://www.instagram.com/accounts/web_create_ajax/', proxies=proxy, headers={'referer':'https://www.instagram.com/accounts/login', 'origin':'https://www.instagram.com/', 'x-csrftoken':data.cookies['csrftoken'], 'x-instagram-ajax': '1', 'x-requested-with': 'XMLHttpRequest', 'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1'}, cookies=data.cookies, data={'email':user+'@gmail.com', 'password':user+'x', 'username':user, 'fullName':user})

def check(data, user, proxy):
	return requests.post('https://www.instagram.com/accounts/web_create_ajax/attempt/', proxies=proxy, headers={'referer':'https://www.instagram.com/accounts/login', 'origin':'https://www.instagram.com/', 'x-csrftoken':data.cookies['csrftoken'], 'x-instagram-ajax': '1', 'x-requested-with': 'XMLHttpRequest', 'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1'}, cookies=data.cookies, data={'email':user+'@gmail.com', 'password':user+'x', 'username':user, 'first_name':user})

def follow(data, user, proxy):
	return requests.post('https://www.instagram.com/web/friendships/'+user+'/follow/', proxies=proxy, cookies=data.cookies, headers={'referer':'https://www.instagram.com', 'origin':'https://www.instagram.com/', 'x-csrftoken':data.cookies['csrftoken'], 'x-instagram-ajax': '1', 'x-requested-with': 'XMLHttpRequest', 'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1'}).status_code

def comment(data, user, proxy, commento):
	return requests.post('https://www.instagram.com/web/comments/'+user+'/add/', proxies=proxy, cookies=data.cookies, headers={'referer':'https://www.instagram.com', 'origin':'https://www.instagram.com/', 'x-csrftoken':data.cookies['csrftoken'], 'x-instagram-ajax': '1', 'x-requested-with': 'XMLHttpRequest', 'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1'}, data={'comment_text':commento}).status_code

def like(data, user, proxy):
	return requests.post('https://www.instagram.com/web/likes/'+user+'/like/', proxies=proxy, cookies=data.cookies, headers={'referer':'https://www.instagram.com', 'origin':'https://www.instagram.com/', 'x-csrftoken':data.cookies['csrftoken'], 'x-instagram-ajax': '1', 'x-requested-with': 'XMLHttpRequest', 'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1'}).status_code

def job(uid, mode):
	global proxy
	pxy = random.choice(proxy)
	if "~" in pxy:
		pxy = pxy.split("~")[0]
	pxyd = {"http":"http://"+pxy, "https":"https://"+pxy, "ftp":"ftp://"+pxy}
	user = randomUsername()
	registerx = register(cookie(pxyd), user, pxyd)
	data = json.loads(registerx.text)

	if data['account_created'] == True:
		safe_print('Account created successfully: @' + user)
		a = 0
		tx = ''
		if mode == 'f':
			a = follow(registerx, uid, pxyd)
			tx = 'Followed'
		elif mode == 'l':
			a = like(registerx, uid, pxyd)
			tx = 'Liked'
		elif mode == 'c':
			a = comment(registerx, uid, pxyd, cm)
			tx = 'Commented'
		b = ('ACCEPTED' if a==200 else 'DECLINED')
		safe_print(tx+' by @' + user + ' (' + b + ')')
	else:
		pass
		#do whatever you want

def main(uid, mode):
	while True:
		try:
			job(uid, mode)
		except Exception as e:
			pass

if __name__ == '__main__':
	print('-'*50+'\n# Instaboom [DEV] b1.3')
	uid = ''
	threads = 0
	mode = ''
	try:
		usr = sys.argv[1]
		threads = int(sys.argv[2])
		pxl = sys.argv[3]
		mode = sys.argv[4]
		proxy = open(pxl, 'r').read().split('\n')
		
		if mode == 'f':
			fff = requests.get('https://www.instagram.com/' + usr).text
			uid = fff.split(', "id": "')[1].split('"')[0]
			print('# Botting @' + usr + ' (' + uid + ') with '+str(threads)+' threads and ' + str(len(proxy)) + ' proxies'+'\n'+'-'*50)
		elif mode == 'l':
			fff = requests.get('https://www.instagram.com/p/' + usr).text
			uid = fff.split('instagram://media?id=')[1].split('"')[0]
			print('# Botting likes on ' + usr + ' (' + uid + ') with '+str(threads)+' threads and ' + str(len(proxy)) + ' proxies'+'\n'+'-'*50)
		elif mode == 'c':
			fff = requests.get('https://www.instagram.com/p/' + usr).text
			uid = fff.split('instagram://media?id=')[1].split('"')[0]
			cm = raw_input("comment: ")
			print('# Botting comments on ' + usr + ' (' + uid + ') with '+str(threads)+' threads and ' + str(len(proxy)) + ' proxies'+'\n'+'-'*50)
		else:
			print('# What? Modes: l (like), f (follow), c (comment)')
			exit(1)
	except Exception as e:
		print("# Something went wrong : " + str(e) + "\npython instaboom.py <account/post> <threads> <proxy file> <mode>")
		exit(1)
	for x in range(0,threads):
		t = threading.Thread(target=main, args=(uid,mode,),)
		t.start()	
	
