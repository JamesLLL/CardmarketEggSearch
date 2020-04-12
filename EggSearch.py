import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

# get user cookies to add to requests
usr_cfduid = input('Enter your __cfduid cookie value: ')
usr_PHPSESSID = input('Enter your PHPSESSID cookie value: ')

# get user agent to allow session to persist (voids session if doesn't match)
usr_userAgent = input('Enter your browsers User-Agent value: ')
print('') # empty line

# prepare for scrape
productPages = []
errorPages = []
foundPage = ''
loggedSeen = False
found = False

with open('links.txt', 'r') as file:
	productPages = file.readlines()

totalPages = len(productPages)
page = 1

# loop through pages and check for egg
for cardPage in productPages:
	# strip trailing new line character so url works
	url = cardPage.rstrip()

	# make the request for current url
	# dunno if all header stuff needed but just incase
	headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
				'Accept-Encoding': 'gzip, deflate, br',
				'Accept-Language': 'en-GB,en;q=0.5',
				'Connection': 'keep-alive',
				'Cookie': 'cookies_consent=accepted; __cfduid=' + usr_cfduid + '; PHPSESSID=' + usr_PHPSESSID,
				'DNT': '1',
				'Host': 'www.cardmarket.com',
				'Referer': 'https://www.cardmarket.com/',
				'Upgrade-Insecure-Requests': '1',
				'User-Agent': usr_userAgent} # user agent must match one of which sessionid was created with
	cookies = {'__cfduid': usr_cfduid,
				'PHPSESSID': usr_PHPSESSID}
	response = requests.get(url, headers=headers, cookies=cookies)
	html_doc = response.content

	# soup the doc content
	soup = BeautifulSoup(html_doc, 'html.parser')

	# check if session is still alive by searching for logged in name span elm
	loggedIn = soup.select('#account-dropdown > div:nth-child(2) > span:nth-child(1)')
	if not loggedIn:
		# display error and log page which failed
		print(' -- Not Logged In! -- ')
		errorPages.append(url)
		loggedSeen = False
	elif not loggedSeen:
		# if first time login or logged in after a fail output to confirm
		print(' -- Logged in as ' + loggedIn[0].contents[0] + ' --')
		loggedSeen = True

	# display product url and name if present
	print(url)
	productName = soup.select('.flex-grow-1 > h1:nth-child(1)')
	if productName:
		print(productName[0].contents[0])
	else:
		print('Unknown Product Name')

	# check for the egg on page via either its id, class, or img src
	egg = soup.find_all(id='EasterEggBox')
	egg2 = soup.find_all(class_='easterEggModal')
	egg3 = soup.select('img[src*="Easter_2020-reward"]') # middle match
	if egg or egg2 or egg3:
		# if found egg then log where and break out of loop
		print('Egg found!\n')
		foundPage = url
		found = True
		break

	print('Page: {} / {}\n'.format(page, totalPages))
	sleep(randint(1,2))
	page += 1

print(' --')
print('Finished.')

if found:
	# save found page to text file
	with open('found.txt', 'a') as file:
		print(foundPage, file=file)
	print('Found on page: {} / {}'.format(page, totalPages))
	print('Check found.txt for page url with egg.')
elif len(errorPages) > 0:
	# save not logged in product pages array to text file
	print('Not found. Replace links.txt with missed.txt and rerun.')
	with open('missed.txt', 'a') as file:
		print(*errorPages, sep='\n', file=file)
else:
	# egg wasn't found
	print('Not found.')