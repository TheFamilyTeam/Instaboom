import threading
import argparse
import requests
import random
import time
import sys

class Instaboom:
	s = requests.session()
	def __init__(self, proxy):
		self.s.headers = {
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9',
			'Referer': 'https://www.instagram.com',
			'Origin': 'https://www.instagram.com',
			'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1',
			'Accept': '*/*',
			'x-requested-with': 'XMLHttpRequest',
		}
		self.s.cookies['ig_cb'] = '1'
		if proxy is not None:
			self.s.proxies = {"http": "http://" + proxy, "https":"https://" + proxy, "ftp":"ftp://" + proxy}
		f = self.s.get('https://www.instagram.com/web/__mid/')
	
	def randomInfo(self):
		nomi = [
			'Francesco', 'Leonardo', 'Alessandro',
			'Lorenzo', 'Mattia', 'Andrea',
			'Gabriele', 'Riccardo', 'Matteo',
			'Tommaso', 'Edoardo', 'Federico',
			'Giuseppe', 'Antonio', 'Diego', 'Nicolo\'',
			'Giovanni', 'Samuele', 'Pietro',
			'Marco', 'Filippo', 'Luca',
			'Michele', 'Simone', 'Alessio',
			'Gabriel', 'Emanuele', 'Giulio',
			'Salvatore', 'Vincenzo', 'Jacopo',
			'Manuel', 'Giacomo', 'Gioele',
			'Thomas', 'Daniele', 'Cristian',
			'Elia', 'Samuel', 'Giorgio',
			'Enea', 'Luigi', 'Daniel',
			'Nicola', 'Stefano', 'Domenico',
			'Raffaele', 'Kevin', 'Sofia',
			'Giulia', 'Aurora', 'Alice',
			'Ginevra', 'Emma', 'Giorgia',
			'Greta', 'Martina', 'Beatrice',
			'Anna', 'Chiara', 'Sara',
			'Nicole', 'Ludovica', 'Gaia',
			'Matilde', 'Vittoria', 'Noemi', 
			'Francesca', 'Alessia', 'Camilla',
			'Bianca', 'Arianna', 'Rebecca',
			'Elena', 'Viola', 'Mia',
			'Elisa', 'Giada', 'Adele',
			'Marta', 'Isabel', 'Melissa',
			'Carlotta', 'Eleonora', 'Miriam',
			'Emily', 'Irene', 'Margherita',
			'Anita', 'Benedetta','Caterina',
			'Azzurra', 'Eva', 'Rachele', 'Cecilia'
		]
		
		cognomi = [
			'Rossi', 'Russo', 'Ferrari', 
			'Esposito', 'Bianchi', 'Romano', 
			'Colombo', 'Ricci', 'Marino', 
			'Greco', 'Bruno', 'Gallo', 
			'Conti', 'DeLuca', 'Mancini', 
			'Costa', 'Giordano', 'Rizzo', 
			'Lombardi', 'Moretti', 'Barbieri', 
			'Fontana', 'Santoro', 'Mariani', 
			'Rinaldi', 'Caruso', 'Ferrara', 
			'Galli', 'Martini', 'Leone', 
			'Longo', 'Gentile', 'Martinelli', 
			'Vitale', 'Lombardo', 'Serra', 
			'Coppola', 'DeSantis', 'Dangelo', 
			'Marchetti', 'Parisi', 'Villa', 
			'Conte', 'Ferraro', 'Ferri', 
			'Fabbri', 'Bianco', 'Marini', 
			'Grasso', 'Valentini', 'Messina', 
			'Sala', 'DeAngelis', 'Gatti', 
			'Pellegrini', 'Palumbo', 'Sanna', 
			'Farina', 'Rizzi', 'Monti', 
			'Cattaneo', 'Morelli', 'Amato', 
			'Silvestri', 'Mazza', 'Testa', 
			'Grassi', 'Pellegrino', 'Carbone', 
			'Giuliani', 'Benedetti', 'Barone', 
			'Rossetti', 'Caputo', 'Montanari', 
			'Guerra', 'Palmieri', 'Bernardi', 
			'Martino', 'Fiore', 'DeRosa', 
			'Ferretti', 'Bellini', 'Basile', 
			'Riva', 'Donati', 'Piras', 
			'Vitali', 'Battaglia', 'Sartori', 
			'Neri', 'Costantini', 'Milani', 
			'Pagano', 'Ruggiero', 'Sorrentino', 
			'Damico', 'Orlando', 'Damico', 'Negri'
		]
		
		formati = ['._%s', '.%s', '_%s', '__%s', '._.%s', '_.%s']
		domini = ['gmail.com', 'libero.it', 'alice.it', 'tim.it', 'tiscali.it']
		anni = [str(x) for x in range(2000, 2006)]
		nome = random.choice(nomi)
		anno = random.choice(anni)
		cognome = random.choice(cognomi)
		formato = random.choice(formati)
		username = '%s%s%s%s' % (nome.lower(), cognome.lower(), str(random.randint(0, 1000)), formato % anno)
		email = '%s%s%s@%s' % (nome.lower(), cognome.lower(), str(random.randint(0, 1000)), random.choice(domini))
		password = '%s%s_%s' % (nome, anno[2:], str(random.randint(0, 1000)))
		return {"nome": nome, "cognome": cognome, "anno": anno, "username": username, "email": email, "password": password, "nc": "%s %s" % (nome, cognome)}

	def login(self, username, password):
		self.s.headers['x-instagram-ajax'] = 'f4c28142cf13'
		self.s.headers['x-ig-app-id'] = '936619743392459'
		self.s.headers['x-csrftoken'] = self.s.cookies['csrftoken']
		self.s.headers['referer'] = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
		self.s.headers['content-type'] = 'application/x-www-form-urlencoded'
		data = {
			'username': username,
			'password': password,
			'queryParams': '{"source":"auth_switcher"}',
			'optIntoOneTap': 'true'
		}
		return self.s.post('https://www.instagram.com/accounts/login/ajax/', data=data).json()

	def register(self, email, username, password, first_name):
		self.s.headers['x-instagram-ajax'] = 'f4c28142cf13'
		self.s.headers['x-ig-app-id'] = '936619743392459'
		self.s.headers['x-csrftoken'] = self.s.cookies['csrftoken']
		self.s.headers['referer'] = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
		self.s.headers['content-type'] = 'application/x-www-form-urlencoded'
		data = {
			'email': email,
			'password': password,
			'username': username,
			'first_name': first_name,
			'client_id': self.s.cookies['mid'],
			'seamless_login_enabled': '1',
			'gdpr_s': '[0,2,0,null]',
			'tos_version': 'eu',
			'opt_into_one_tap': 'false'
		}
		return self.s.post('https://www.instagram.com/accounts/web_create_ajax/', data=data).json()
	
	def follow(self, username):
		self.s.headers['x-instagram-ajax'] = 'f4c28142cf13'
		self.s.headers['x-ig-app-id'] = '936619743392459'
		self.s.headers['x-csrftoken'] = self.s.cookies['csrftoken']
		self.s.headers['referer'] = 'https://www.instagram.com/' + username
		self.s.headers['content-type'] = 'application/x-www-form-urlencoded'
		r = requests.get('https://instagram.com/' + username).text
		userId = r.split('profilePage_')[1].split('"')[0]
		flw = self.s.post('https://www.instagram.com/web/friendships/%s/follow/' % userId)
		return flw.json()
	
	def like(self, postId):
		self.s.headers['x-instagram-ajax'] = 'f4c28142cf13'
		self.s.headers['x-ig-app-id'] = '936619743392459'
		self.s.headers['x-csrftoken'] = self.s.cookies['csrftoken']
		self.s.headers['referer'] = 'https://www.instagram.com/p/' + postId
		self.s.headers['content-type'] = 'application/x-www-form-urlencoded'
		r = requests.get('https://instagram.com/p/' + postId).text
		id = r.split('<meta property="al:ios:url" content="instagram://media?id=')[1].split('"')[0]
		like = self.s.post('https://www.instagram.com/web/likes/%s/like/' % id)
		return like.json()

def usage(r):
	print("[!] %s\n[i] Usage: python %s -m <mode, follow/like> -u <user, follow only> -pi <post, like only> -p <proxy list> -a <account list file, optional>" % (r, " ".join(sys.argv)))

def lFollow(acc, i):
	d = acc.rstrip().lstrip().split(':')
	email = d[0]
	password = d[1]
	print('[***] Logging in %s...' % acc)
	a = i.login(email, password)
	if 'authenticated' in a:
		if a['authenticated']:
			print('[***] Following %s...\n' % args.user)
			i.follow(args.user)
	elif a['message'] == 'checkpoint_required':
		print('[***] Instagram blocked the login, reason: locked account.\n')
	elif['showAccountRecoveryModal']:
		print('[***] Instagram blocked the login, reason: recovery mode.\n')
	else:
		print('[***] Instagram blocked the login, reason: wrong email/password.\n')

def followThread(args):
	if args.user:
		i = Instaboom(proxy)
		if not args.acclist:
			while True:
				data = i.randomInfo()
				print('[***] Registering %s (%s)...' % (data['username'], data['nc']))
				a = i.register(data['email'], data['username'], data['password'], data['nc'])
				if a['account_created']:
					print('[***] Following %s...\n' % args.user)
					i.follow(args.user)
				else:
					print('[***] Instagram blocked the registration, reason: %s.\n' % ', '.join(a['errors'].keys()))
		else:
			accs = open(args.acclist, 'r').read().splitlines()
			for acc in accs:
				threading.Thread(target=lFollow, args=(acc, i,),).start()
				time.sleep(0.25)
	else:
		usage("No user was specified")

def lLike(acc, i):
	d = acc.rstrip().lstrip().split(':')
	email = d[0]
	password = d[1]
	print('[***] Logging in %s...' % acc)
	a = i.login(email, password)
	if 'authenticated' in a:
		if a['authenticated']:
			print('[***] Liking %s...\n' % args.post)
			i.like(args.post)
		elif a['message'] == 'checkpoint_required':
			print('[***] Instagram blocked the login, reason: locked account.\n')
		elif['showAccountRecoveryModal']:
			print('[***] Instagram blocked the login, reason: recovery mode.\n')
		else:
			print('[***] Instagram blocked the login, reason: wrong email/password.\n')

def likeThread(args):
	if args.post:
		i = Instaboom(proxy)
		if not args.acclist:
			while True:
				data = i.randomInfo()
				print('[***] Registering %s (%s)...' % (data['username'], data['nc']))
				a = i.register(data['email'], data['username'], data['password'], data['nc'])
				if a['account_created']:
					print('[***] Liking %s...\n' % args.post)
					i.like(args.post)
				else:
					print('[***] Instagram blocked the registration, reason: %s.\n' % ', '.join(a['errors'].keys()))
		else:
			accs = open(args.acclist, 'r').read().splitlines()
			for acc in accs:
				threading.Thread(target=lLike, args=(acc, i,),).start()
				time.sleep(0.25)
	else:
		usage("No post ID was specified")

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Instaboom - Instagram follow bot')
	parser.add_argument('-mode', '-m', help='bot mode', action='store')
	parser.add_argument('-user', '-u', help='user to follow', action='store')
	parser.add_argument('-post', '-pi', help='post id to like', action='store')
	parser.add_argument('-proxies', '-p', help='proxy list file', action='store')
	parser.add_argument('-acclist', '-a', help='account list fle', action='store')
	args = parser.parse_args()
	
	print("""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
  _____           _        _                           
 |_   _|         | |      | |                          
   | |  _ __  ___| |_ __ _| |__   ___   ___  _ __ ___  
   | | | '_ \/ __| __/ _` | '_ \ / _ \ / _ \| '_ ` _ \ 
  _| |_| | | \__ \ || (_| | |_) | (_) | (_) | | | | | |
 |_____|_| |_|___/\__\__,_|_.__/ \___/ \___/|_| |_| |_| 3.0
                                                       
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
	print("[i] Created by Neon and TheFamilyTeam")
	print("[-] https://github.com/TheFamilyTeam")
	print("[-] https://github.com/prefisso")
	print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	
	try:
		if args.proxies:
			proxy = random.choice(open(args.proxies, 'r').read().split('\n'))
		else:
			proxy = None
		
		if args.mode is None:
			usage("No mode was specified")
		elif args.mode == 'follow':
			threading.Thread(target=followThread, args=(args,),).start()
		elif args.mode == 'like':
			threading.Thread(target=likeThread, args=(args,),).start()
		else:
			usage("Invalid mode")
	except Exception as e:
		print('[!] Something went wrong: %s.' % e)
	
